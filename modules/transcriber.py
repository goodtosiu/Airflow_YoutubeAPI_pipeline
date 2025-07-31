# modules/transcriber.py
import whisper

def generate_subtitle(video_path: str, output_path: str):
    model = whisper.load_model("base")  # medium, large 로 바꿀 수도 있음
    result = model.transcribe(video_path)
    with open(output_path, "w") as f:
        for segment in result["segments"]:
            f.write(f"{segment['start']} --> {segment['end']}\n")
            f.write(segment["text"] + "\n\n")