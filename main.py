from pytube import YouTube

def main(link):
    yt = YouTube(link)
    video_title = yt.title
    print(f"Video title: {video_title}")
    video_stream = yt.streams.filter(only_audio=True).first()
    output_file = f"{video_title}.mp3"
    print(f"[script] downloading {video_title}")

    video_stream.download(filename=output_file, filename_prefix="")
    # Calculate file size
    video_size_mb = video_stream.filesize / (1024 * 1024)  # Convert bytes to megabytes
    print(f"\nFile size: {video_size_mb:.2f} MB")
if __name__ == '__main__':
    while True:
     link = input("Enter your link: ")
     main(link)
