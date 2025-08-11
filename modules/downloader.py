from yt_dlp import YoutubeDL

def download_video(video_url):
    ydl_opts = {
        'cookiefile': '/opt/airflow/cookies/www.youtube.com_cookies.txt',
        'format': 'bestaudio[ext=m4a]/bestaudio',
        'outtmpl': '/opt/airflow/data/videos/%(id)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',  # 최종은 mp3로 통일
            'preferredquality': '192',
        }],
        'noplaylist': True,
        'verbose': True,
        'postprocessor_args': ['-y'],  # 덮어쓰기
        'keepvideo': False,              # 변환 후 원본 파일 삭제
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
    }

    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    info = ydl.extract_info(video_url, download=True)
    video_id = info.get('id')
    final_path = f"/opt/airflow/data/videos/{video_id}.mp3"
    return final_path   