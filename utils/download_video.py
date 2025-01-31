import os
import yt_dlp
import uuid

def download_video(video_url, save_path=None, resolution='720p'):
    # If save_path is None, create a default folder in the current directory
    if save_path is None:
        save_path = os.path.join(os.getcwd(), "Downloaded_Videos")
    
    # Create the folder if it doesn't exist
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    # Generate a unique identifier for the filename
    unique_id = uuid.uuid4()
    
    # yt-dlp options for downloading the video with proper MP4 encoding
    ydl_opts = {
        # Format selection prioritizing MP4 codec
        'format': f'bestvideo[height<={resolution[:-1]}][vcodec^=avc1]+bestaudio[acodec^=mp4a]/best[ext=mp4]/best',
        # Force encoding to MP4 container
        'merge_output_format': 'mp4',
        # Ensure proper encoding with FFmpeg
        'postprocessors': [{
            'key': 'FFmpegVideoRemuxer',
            'preferedformat': 'mp4',
        }],
        # Force re-encoding if necessary
        'postprocessor_args': [
            '-c:v', 'libx264',  # Force H.264 video codec
            '-c:a', 'aac',      # Force AAC audio codec
            '-movflags', '+faststart'  # Enable streaming-friendly format
        ],
        # Output template
        'outtmpl': os.path.join(save_path, '%(title)s') + f'_{unique_id}.%(ext)s',
        'quiet': False,
        'no_warnings': True,
        'logger': None
    }

    # Downloading the video
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print(f"Video downloaded successfully to: {save_path}")
    except Exception as e:
        print(f"Failed to download video: {str(e)}")

# Example usage:
video_url = 'https://youtu.be/K5KAc5CoCuk?si=1LH0Ip9xNf6FRfmB'
download_path = "Downloads"
download_video(video_url, download_path, resolution='480p')