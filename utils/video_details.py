import yt_dlp

def get_youtube_info(video_url):
    with yt_dlp.YoutubeDL({'quiet': True, 'no_warnings': True, 'logger': None}) as ydl:
        info = ydl.extract_info(video_url, download=False)
        title = info.get('title')
        thumbnail_url = info.get('thumbnail')
        
        # Extract available resolutions and sizes
        resolutions = {}
        for f in info.get('formats', []):
            height = f.get('height')
            filesize = f.get('filesize')
            if height is not None:
                if height >= 240:
                    resolution = f'{height}p'
                    # Convert filesize to a human-readable format (if available)
                    size = "Unknown size"
                    if filesize is not None:
                        if filesize >= 1_073_741_824:  # GB
                            size = f"{filesize / 1_073_741_824:.2f} GB"
                        elif filesize >= 1_048_576:  # MB
                            size = f"{filesize / 1_048_576:.2f} MB"
                        elif filesize >= 1_024:  # KB
                            size = f"{filesize / 1_024:.2f} KB"
                        else:
                            size = f"{filesize} bytes"

                    resolutions[resolution] = size

    return title, thumbnail_url, resolutions

# Example usage
video_url = 'https://youtu.be/K5KAc5CoCuk?si=uJu_kxapIHd2KExM'
title, thumbnail_url, resolutions = get_youtube_info(video_url)

print(f"Title: {title}\nThumbnail URL: {thumbnail_url}\nAvailable Resolutions and Sizes: {resolutions}")
