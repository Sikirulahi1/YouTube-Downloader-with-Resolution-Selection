from pytube import YouTube

# Function for downloading the video
def download_video(video_url, save_path, resolution_choice):
    try:
        youtube = YouTube(video_url)
        video_stream = youtube.streams.get_by_resolution(resolution_choice)
        video_stream.download(output_path = save_path)
        print("Video downloaded successfully")
    except Exception as e:
        print("Failed to download video :" + str(e))

# Function to download the audio file
def download_audio(video_url, save_path):
    try:
        youtube = YouTube(video_url)
        audio = youtube.streams.filter(only_audio = True).first()
        audio.download(output_path =save_path)
        print("Downloaded Sussesfully")
    except Exception as e:
        print("Failed to download Audio :" + str(e))
    
    
# The main function
def main():
    print("This is a Youtube downloader app cleated by Sikirulahi")
    print("Gmail: kareemsikiru2018@gmail.com")
    video_url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the path to save the downloaded content: ")
    print("\n 1. Download video")
    print("2. Download audio")
    choice = input("choose between (1/2):")
    
    if choice == "1":
        resolution_choice = input("Choose a desired resolution(e.g., 720p, 1080p):")
        download_video(video_url, save_path, resolution_choice)
    elif choice == "2":
        download_audio(video_url, save_path)
    else:
        print("Invalid Choice, Please choose")
    
if __name__ == "__main__":
    main()