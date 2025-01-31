import yt_dlp

def get_playlist_video_links(playlist_url):
    ydl_opts = {
        'extract_flat': True,  # Only list the videos, do not download them
        'quiet': True,         # Suppress most output
        'no_warnings': True,   # Suppress warnings
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(playlist_url, download=False)
        
        # Ensure the result is a playlist
        if 'entries' in result:
            video_urls = [entry['url'] for entry in result['entries']]
            return video_urls
        else:
            print("The provided URL is not a playlist.")
            return []

# Example usage
playlist_url = "https://youtube.com/playlist?list=PLZoTAELRMXVPBTrWtJkn3wWQxZkmTXGwe&si=KeNXI9e4XpM-MjwJ"
video_links = get_playlist_video_links(playlist_url)

# Print or use the video links
for link in video_links:
    print(link)

for video_url in video_links:
    title, thumbnail_url, resolutions = get_youtube_info(video_url)
    print(f"Title: {title}\nThumbnail URL: {thumbnail_url}\nAvailable Resolutions and Sizes: {resolutions}")
    print("--------------------------------------------------------")