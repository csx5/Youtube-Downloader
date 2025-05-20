from pytube import YouTube
from pytube.cli import on_progress
from colorama import Fore, Style, init
import sys
import os

init(autoreset=True)

def print_banner():
    print(Fore.CYAN + "\n===YouTube Downloader ===\n" + Style.RESET_ALL)

def show_video_info(yt):
    print(Fore.YELLOW + "\n--- Video Info ---")
    print(Fore.GREEN + f"Title       : {yt.title}")
    print(Fore.GREEN + f"Author      : {yt.author}")
    print(Fore.GREEN + f"Length      : {yt.length} seconds")
    print(Fore.GREEN + f"Views       : {yt.views}")
    print(Fore.GREEN + f"Published   : {yt.publish_date}")
    print(Fore.YELLOW + "------------------\n")

def list_resolutions(yt):
    streams = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc()
    print(Fore.BLUE + "Available resolutions:")
    for i, stream in enumerate(streams):
        print(Fore.CYAN + f"{i+1}. {stream.resolution} - {stream.mime_type} - {round(stream.filesize / (1024*1024), 2)} MB")
    return streams

def download_menu(yt):
    show_video_info(yt)
    print(Fore.MAGENTA + "Choose download option:")
    print("1. Best Quality (video + audio)")
    print("2. Audio Only")
    print("3. Select Resolution")

    choice = input(Fore.WHITE + "Your choice: ")
    
    if choice == "1":
        stream = yt.streams.get_highest_resolution()
    elif choice == "2":
        stream = yt.streams.filter(only_audio=True).first()
    elif choice == "3":
        streams = list_resolutions(yt)
        selection = input(Fore.WHITE + "Select resolution number: ")
        if not selection.isdigit() or int(selection) < 1 or int(selection) > len(streams):
            print(Fore.RED + "Invalid selection.")
            return
        stream = streams[int(selection)-1]
    else:
        print(Fore.RED + "Invalid choice.")
        return

    print(Fore.YELLOW + "\nDownloading... Please wait.")
    stream.download()
    print(Fore.GREEN + "\n✅ Download complete!")

def start_downloader():
    print_banner()
    while True:
        url = input(Fore.WHITE + "Enter YouTube URL (or type 'exit' to quit): ")
        if url.lower() == "exit":
            print(Fore.CYAN + "Goodbye!")
            sys.exit()
        try:
            yt = YouTube(url, on_progress_callback=on_progress)
            download_menu(yt)
        except Exception as e:
            print(Fore.RED + f"Error: {e}")

if __name__ == "__main__":
    start_downloader()
