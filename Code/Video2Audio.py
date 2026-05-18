import os
from pathlib import Path
from moviepy import VideoFileClip

def extract_audio():
    # Define directories
    base_dir = Path(__file__).parent.parent
    videos_dir = base_dir / "Assets" / "Videos"
    audio_dir = base_dir / "Assets" / "Audio"
    
    # Ensure audio directory exists
    audio_dir.mkdir(parents=True, exist_ok=True)
    
    # Supported video formats
    video_extensions = {".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"}
    
    # Find all videos
    video_files = []
    if videos_dir.exists():
        for ext in video_extensions:
            video_files.extend(videos_dir.rglob(f"*{ext}"))
    
    if not video_files:
        print(f"No video files found in {videos_dir}")
        return

    print(f"Found {len(video_files)} video files. Starting extraction...")
    
    for video_path in video_files:
        # Create corresponding output path
        rel_path = video_path.relative_to(videos_dir)
        audio_path = audio_dir / rel_path.with_suffix('.mp3')
        
        # Ensure subdirectories exist
        audio_path.parent.mkdir(parents=True, exist_ok=True)
        
        if audio_path.exists():
            print(f"Skipping (already exists): {audio_path.name}")
            continue
            
        print(f"Extracting: {video_path.name} -> {audio_path.name}")
        try:
            # Load video and extract audio
            with VideoFileClip(str(video_path)) as video:
                if video.audio is not None:
                    video.audio.write_audiofile(str(audio_path), logger=None)
                    print(f"Successfully extracted to {audio_path.name}")
                else:
                    print(f"No audio track found in {video_path.name}")
        except Exception as e:
            print(f"Failed to process {video_path.name}. Error: {e}")

if __name__ == '__main__':
    extract_audio()
