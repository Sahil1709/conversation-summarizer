import os
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

client = Groq(
    api_key=os.getenv("API_KEY"),
)
print(os.getenv("API_KEY"))
filename = os.path.dirname(__file__) + "/Recording.m4a"
print(filename)

with open(filename, "rb") as file:
    transcription = client.audio.transcriptions.create(
      file=(filename, file.read()),
      model="whisper-large-v3",
      response_format="verbose_json",
    )
    print(transcription)
    # avg_logprob // closer to 0 is better
    # no_speech_prob // closer to 0 is better
    # print(transcription.text)
    # print(transcription.segments)

      