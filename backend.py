from fastapi import FastAPI, File, UploadFile
import os
from groq import Groq
from dotenv import load_dotenv
import tempfile
load_dotenv()

app = FastAPI()

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    # Create a temporary file in the appropriate system directory
    with tempfile.NamedTemporaryFile(suffix=".m4a", delete=False) as temp_file:
        temp_file_path = temp_file.name
        temp_file.write(await file.read())

    # Call Groq API to transcribe
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )
    with open(temp_file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=(file.filename, audio_file.read()),
            model="whisper-large-v3",
            response_format="verbose_json",
        )

    

    os.remove(temp_file_path)

    # Return the transcription
    print(transcription)
    return {
        "transcription": transcription.text,
        "segments": transcription.segments,
        "language": transcription.language,
        "duration": transcription.duration,
        "task": transcription.task
    }
