from __future__ import annotations

from pathlib import Path


def collect_full_txt_files(root_dir: Path) -> list[Path]:
	return sorted(
		(
			path
			for path in root_dir.rglob("*full.txt")
			if path.is_file()
		),
		key=lambda path: path.relative_to(root_dir).as_posix(),
	)


def merge_full_txt_files(root_dir: Path, output_file: Path) -> int:
	files = collect_full_txt_files(root_dir)
	merged_text = ""
	for file in files:
		text = file.read_text(encoding="utf-8")
		merged_text += "文件: " + file.name + "\n\n" + text.replace("\n", '') + "\n\n"

	output_file.write_text(merged_text, encoding="utf-8")
	return len(files)


def main() -> None:
	script_dir = Path(__file__).resolve().parent
	output_file = script_dir / "combined.txt"
	merged_count = merge_full_txt_files(script_dir, output_file)
	print(f"已合并 {merged_count} 个文件到 {output_file}")


if __name__ == "__main__":
	main()
