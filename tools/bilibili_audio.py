from fastapi import APIRouter, Query
from fastapi.responses import FileResponse
import yt_dlp
import uuid
import os

router = APIRouter()

TMP_DIR = "tmp"

@router.get("/")
async def extract_audio(url: str = Query(..., description="B站视频链接")):
    video_id = str(uuid.uuid4())
    output_path = os.path.join(TMP_DIR, f"{video_id}.mp3")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(TMP_DIR, f"{video_id}.%(ext)s"),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': '/usr/bin/ffmpeg',  # 显式指定路径
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    return FileResponse(output_path, filename=f"bilibili-audio.mp3", media_type="audio/mpeg")
