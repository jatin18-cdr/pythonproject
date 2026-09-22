"""# Step 1: Record audio from microphone

# Dependencies: ffmpeg, portaudio, pyaudio

import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO
from pathlib import Path

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def record_audio(file_path, timeout=20, phrase_time_limit=None):
    """ """
    Record audio from the microphone and save it as an MP3 file.

    Args:
        file_path (str): Output MP3 file path.
        timeout (int): Maximum wait time for speech.
        phrase_time_limit (int): Maximum recording duration.
    """"""""

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        logging.info("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)

        logging.info("🎤 Speak now...")

        audio = recognizer.listen(
            source,
            timeout=timeout,
            phrase_time_limit=phrase_time_limit
        )

    # Convert WAV bytes to MP3
    wav_buffer = BytesIO(audio.get_wav_data())
    audio_segment = AudioSegment.from_file(wav_buffer, format="wav")
    audio_segment.export(file_path, format="mp3")

    logging.info(f"✅ Audio saved to {file_path}")


if __name__ == "__main__":
    output_file = Path(__file__).with_name("patient_voice.mp3")
    record_audio(str(output_file), timeout=20)

 # Step 2: Convert audio to text

from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

groq_api_key = os.environ.get("GROQ_API_KEY")

client = Groq(api_key=groq_api_key)

audio_filepath = "patient_voice.mp3"

with open(audio_filepath, "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model=os.environ.get("WHISPER_MODEL", "whisper-large-v3"),
    )

print(transcription.text)"""

# Step 1: Record audio and convert it to text

import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()


def transcribe_patient_voice(audio_filepath):
    """
    Convert a patient's audio file to text using Groq Whisper.

    Args:
        audio_filepath (str): Path to the uploaded/recorded audio file.

    Returns:
        str: Transcribed text.
    """

    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("Missing GROQ_API_KEY in .env")

    client = Groq(api_key=groq_api_key)

    with open(audio_filepath, "rb") as audio_file:
        transcription = client.audio.transcriptions.create(
            file=audio_file,
            model=os.getenv("WHISPER_MODEL", "whisper-large-v3"),
        )

    return transcription.text