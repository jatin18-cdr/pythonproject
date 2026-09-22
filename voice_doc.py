"""from deepgram import DeepgramClient
from dotenv import load_dotenv
from pathlib import Path
import os

# Step 1: Load environment variables
load_dotenv()

text = "Hi, my name is AI with Jatin, who are you?"

api_key = os.getenv("DEEPGRAM_API_KEY")
deepgram = DeepgramClient(api_key=api_key)

# Step 2: Generate speech
audio = deepgram.speak.v1.audio.generate(
    text=text,
    model="aura-2-thalia-en",
    encoding="mp3",
)

# Step 3: Save audio
from pathlib import Path 
audio_file = "test-output.mp3"
audio_path=Path(__file__).with_name(audio_file)
with audio_path.open("wb") as file:
    for chunk in audio:
        file.write(chunk)
# Step 4: play audio
import platform
import subprocess

# Play the generated audio on macOS
if platform.system() == "Darwin":
    subprocess.run(["afplay", str(audio_path)])"""
import os
import platform
import subprocess
from pathlib import Path

from deepgram import DeepgramClient
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


def convert_text_to_doctor_audio(text, output_file="test-output.mp3"):
    """
    Convert doctor's text response into an MP3 using Deepgram.
    """

    api_key = os.getenv("DEEPGRAM_API_KEY")
    if not api_key:
        raise ValueError("Missing DEEPGRAM_API_KEY in .env")

    deepgram = DeepgramClient(api_key=api_key)

    audio = deepgram.speak.v1.audio.generate(
        text=text,
        model="aura-2-thalia-en",
        encoding="mp3",
    )

    audio_path = Path(__file__).with_name(output_file)

    with audio_path.open("wb") as file:
        for chunk in audio:
            file.write(chunk)

    return audio_path


def play_audio(audio_path):
    """
    Play the generated audio on macOS.
    """

    if platform.system() == "Darwin":
        subprocess.run(["afplay", str(audio_path)])