#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
PDF to Markdown Converter using GPT Vision API

This script converts each page of a PDF into an image, sends it to a multimodal
LLM (like GPT-5.5) via the OpenAI API, and assembles the returned Markdown.

Requirements:
    pip install openai pymupdf

Usage:
    python pdf_to_markdown.py input.pdf -o output.md --api-key sk-xxx --model gpt-5.5
"""

import argparse
import base64
import io
import json
import sys
import time
from pathlib import Path
from typing import Optional

import fitz  # PyMuPDF
from openai import OpenAI


def pdf_page_to_image_base64(page: fitz.Page, dpi: int = 200) -> str:
    """Render a PDF page to a PNG image and return its base64 data URI."""
    pix = page.get_pixmap(dpi=dpi)
    img_bytes = pix.tobytes("png")
    b64 = base64.b64encode(img_bytes).decode("utf-8")
    return f"data:image/png;base64,{b64}"


def call_vision_api(
    client: OpenAI,
    model: str,
    image_base64: str,
    page_num: int,
    retries: int = 3,
) -> str:
    """Send an image to the vision API and get the Markdown response."""
    messages = [
        {
            "role": "system",
            "content": (
                "你是一个专业的文档转换助手。请将图片中的内容精确地转换为 Markdown 格式，"
                "保留原有的标题、列表、表格、粗体、斜体等结构。不要添加额外解释。"
            ),
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": image_base64},
                },
            ],
        },
    ]

    last_exception = None
    for attempt in range(retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.0,
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            last_exception = e
            wait = 2 ** attempt
            print(f"  [retry {attempt+1}/{retries}] API error: {e}. Waiting {wait}s...")
            time.sleep(wait)

    raise last_exception


def convert_pdf_to_markdown(
    pdf_path: str,
    api_key: str,
    model: str = "gpt-5.5",
    base_url: Optional[str] = None,
    dpi: int = 300,
    output_path: Optional[str] = None,
) -> str:
    """
    Convert all pages of a PDF to Markdown using the GPT vision model.

    Args:
        pdf_path: Path to the input PDF file.
        api_key: API key for the OpenAI-compatible service.
        model: Model name to use for conversion.
        base_url: Custom API base URL (defaults to OpenAI's).
        dpi: Resolution for page rendering (higher = better quality but larger images).
        output_path: Path to write the final Markdown (optional).

    Returns:
        Combined Markdown string from all pages.
    """
    client = OpenAI(api_key=api_key, base_url=base_url)

    # Open PDF
    doc = fitz.open(pdf_path)
    num_pages = len(doc)
    print(f"PDF loaded: {num_pages} pages")

    markdown_parts = []
    out_file = Path(output_path) if output_path else None
    if out_file:
        out_file.parent.mkdir(parents=True, exist_ok=True)
    first_write = True

    for i in range(num_pages):
        page = doc[i]
        print(f"Processing page {i+1}/{num_pages}...")

        # Render page to base64 image
        img_b64 = pdf_page_to_image_base64(page, dpi=dpi)

        # Call vision API
        md_text = call_vision_api(client, model, img_b64, page_num=i + 1)

        # Add a page separator for clarity
        separator = f"\n\n<!-- Page {i+1} -->\n\n"
        page_markdown = separator + md_text
        markdown_parts.append(page_markdown)

        if out_file:
            mode = "w" if first_write else "a"
            with out_file.open(mode, encoding="utf-8") as handle:
                handle.write(page_markdown)
            first_write = False

        # Simple progress or rate limiting
        time.sleep(0.5)

    doc.close()

    # Combine all parts
    full_markdown = "\n".join(markdown_parts)

    # Write to file if output path provided
    if out_file:
        print(f"Markdown saved to: {out_file.resolve()}")

    return full_markdown


def main():
    parser = argparse.ArgumentParser(
        description="Convert PDF to Markdown using GPT vision model"
    )
    parser.add_argument("-pdf", default="Assets/Shen_full_note.pdf", help="Path to the input PDF file")
    parser.add_argument(
        "-o", "--output", default="output.md", help="Output Markdown file path"
    )
    parser.add_argument(
        "--api-key",
        default="sk-GkSFfEtIjOCXF7OZ39AFpX9WqJfPFhZ4JZ0Hmg65QwgjBoZr",
        help="API key for the model provider",
    )
    parser.add_argument(
        "--model", default="gpt-5.5", help="Model name (e.g., gpt-5.5, gpt-4o)"
    )
    parser.add_argument(
        "--base-url",
        default="https://ai-apigateway.must.edu.mo/openhub/v1",
        help="Custom API base URL (default: OpenAI official endpoint)",
    )
    parser.add_argument(
        "--dpi", type=int, default=400, help="DPI for page images (default: 200)"
    )
    args = parser.parse_args()

    try:
        markdown = convert_pdf_to_markdown(
            pdf_path=args.pdf,
            api_key=args.api_key,
            model=args.model,
            base_url=args.base_url,
            dpi=args.dpi,
            output_path=args.output,
        )
        # Print summary
        print(f"Conversion complete. Total length: {len(markdown)} characters.")
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()