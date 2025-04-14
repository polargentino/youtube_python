import yt_dlp
import socket

def descargar_mp3(url):
    config = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': '%(title)s.%(ext)s',
        'retries': 5,
        'socket_timeout': 15,
    }

    try:
        socket.setdefaulttimeout(15)  # Timeout global
        with yt_dlp.YoutubeDL(config) as ydl:
            ydl.download([url])
        print("✅ Descarga completada!")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    url = "https://youtu.be/N4DAi9XArms?si=WdhmBdVFWTD1L5Jz"
    descargar_mp3(url)
