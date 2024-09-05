import streamlit as st
import pandas as pd
import numpy as np
import tempfile
import requests
from st_audiorec import st_audiorec

st.title('Speech to Text')

wav_audio_data = st_audiorec()

if wav_audio_data is not None:
    # Create a temporary file
    with tempfile.NamedTemporaryFile(suffix=".m4a", delete=False) as temp_file:
        temp_file.write(wav_audio_data)
        temp_file_path = temp_file.name
    
    # Display the recorded audio
    st.audio(wav_audio_data, format='audio/m4a')
    
    # Send file to the backend API
    with open(temp_file_path, 'rb') as f:
        files = {'file': f}
        response = requests.post("http://127.0.0.1:8000/transcribe/", files=files)

    # Display the transcription
    response = response.json()
    print(response)
    st.write(response['transcription'])  