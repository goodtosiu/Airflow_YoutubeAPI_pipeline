# modules/downloader.py
import yt_dlp

def download_video(video_url: str, output_path: str):
    ydl_opts = {
        'outtmpl': output_path,
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
