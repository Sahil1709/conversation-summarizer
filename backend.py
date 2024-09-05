from fastapi import FastAPI, File, UploadFile
import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    # Save the uploaded file temporarily
    temp_file_path = f"/tmp/{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Call Groq API to transcribe
    client = Groq(
        api_key=os.getenv("GROQ_API_KEY"),
    )
    with open(temp_file_path, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=(temp_file_path, audio_file.read()),
            model="distil-whisper-large-v3-en",
            response_format="verbose_json",
        )

    # Return the transcription
    print(transcription)
    return {
        "transcription": transcription.text,
        "groq_response": transcription.segments,
    }
