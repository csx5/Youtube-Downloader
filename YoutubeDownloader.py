from pytube import YouTube
import sys

def video_info(yt):
    print("\nVideo-Informationen:")
    print(f"Titel: {yt.title}")
    print(f"Dauer: {yt.length} Sekunden")
    print(f"Aufrufe: {yt.views}")
    print(f"Autor: {yt.author}")
    print(f"Veröffentlicht am: {yt.publish_date}")

def download_video(url):
    try:
        yt = YouTube(url)
        video_info(yt)
        print("\nWähle eine Option:")
        print("1. Beste Auflösung (Video + Audio)")
        print("2. Nur Audio")
        wahl = input("Deine Auswahl: ")

        if wahl == "1":
            stream = yt.streams.get_highest_resolution()
            print("Lade Video herunter...")
            stream.download()
        elif wahl == "2":
            stream = yt.streams.filter(only_audio=True).first()
            print("Lade Audio herunter...")
            stream.download()
        else:
            print("Ungültige Auswahl.")

        print("Download abgeschlossen!")
    except Exception as e:
        print(f"Fehler: {e}")

def hauptmenü():
    while True:
        print("\n=== YouTube Downloader ===")
        print("1. Video herunterladen")
        print("2. Beenden")
        auswahl = input("Bitte wähle eine Option: ")

        if auswahl == "1":
            url = input("Gib die YouTube-URL ein: ")
            download_video(url)
        elif auswahl == "2":
            print("Beende das Programm.")
            sys.exit()
        else:
            print("Ungültige Auswahl. Bitte nochmal.")

if __name__ == "__main__":
    hauptmenü()
