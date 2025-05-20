from pytube import YouTube
from pytube.cli import on_progress
import sys

def print_banner():
    print("\n==============================")
    print("     YouTube Downloader")
    print("==============================\n")

def clean_url(url):
    if "?" in url:
        url = url.split("?")[0]
    if "&" in url:
        url = url.split("&")[0]
    return url

def show_video_info(yt):
    print("\n--- Video Information ---")
    print(f"Title      : {yt.title}")
    print(f"Author     : {yt.author}")
    print(f"Length     : {yt.length} seconds")
    print(f"Views      : {yt.views}")
    print(f"Published  : {yt.publish_date}")
    print("--------------------------\n")

def list_resolutions(yt):
    streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    print("Available video resolutions:")
    for i, stream in enumerate(streams):
        size_mb = round(stream.filesize / (1024 * 1024), 2)
        print(f"{i+1}. {stream.resolution} - {stream.mime_type} - {size_mb} MB")
    return streams

def download_menu(yt):
    show_video_info(yt)
    print("Choose download option:")
    print("1. Best Quality (video + audio)")
    print("2. Audio Only")
    print("3. Select Resolution")

    choice = input("Your choice (1/2/3): ")

    if choice == "1":
        stream = yt.streams.get_highest_resolution()
    elif choice == "2":
        stream = yt.streams.filter(only_audio=True).first()
    elif choice == "3":
        streams = list_resolutions(yt)
        selection = input("Select resolution number: ")
        if not selection.isdigit() or int(selection) < 1 or int(selection) > len(streams):
            print("Invalid selection.")
            return
        stream = streams[int(selection)-1]
    else:
        print("Invalid choice.")
        return

    print("\nDownloading... Please wait.")
    stream.download()
    print("\nDownload complete!")

def start_downloader():
    print_banner()
    while True:
        url = input("Enter YouTube URL (or type 'exit' to quit): ")
        if url.lower() == "exit":
            print("Goodbye!")
            sys.exit()
        try:
            clean = clean_url(url)
            yt = YouTube(clean, on_progress_callback=on_progress)
            download_menu(yt)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    start_downloader()
