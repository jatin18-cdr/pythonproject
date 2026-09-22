import os
import base64
import mimetypes

from dotenv import load_dotenv
from groq import Groq

# Load .env
load_dotenv()


def encode_file(filepath):
    with open(filepath, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")


def get_media_type(filepath, fallback):
    media_type, _ = mimetypes.guess_type(filepath)
    return media_type or fallback


def brain_of_the_doctor(patient_text, image_filepath=None, video_filepath=None):
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("Missing GROQ_API_KEY in .env")

    prompt = (
        "You are a confident, natural doctor specializing in skin care. "
        "Speak with reassurance. "
        "Limit your entire response to two or three sentences maximum. "
        "Do not use special characters, symbols, asterisks, or markdown formatting.\n\n"
        f"Patient text: {patient_text}"
    )

    client = Groq(api_key=groq_api_key)

    # Build Groq content
    content = [{"type": "text", "text": prompt}]

    # Add image if provided
    if image_filepath:
        content.append({
            "type": "image_url",
            "image_url": {
                "url": f"data:{get_media_type(image_filepath, 'image/png')};base64,{encode_file(image_filepath)}"
            }
        })

    response = client.chat.completions.create(
        model=os.getenv("GROQ_MODEL", "qwen/qwen3.8-27b"),
        max_completion_tokens=1000,
        messages=[
            {
                "role": "user",
                "content": content
            }
        ],
    )

    return response.choices[0].message.content


"""# Load .env
folder = os.path.dirname(__file__)
env_path = os.path.join(folder, ".env")
load_dotenv(env_path)

# Get API key
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("Missing GROQ_API_KEY in .env or environment")

# Read image
image_path = os.path.join(folder, "sample-image.png")
with open(image_path, "rb") as file:
    image_data = base64.b64encode(file.read()).decode("utf-8")

# Create Groq client
client = Groq(api_key=api_key)

# Send request
response = client.chat.completions.create(
    model=os.environ.get(
        "GROQ_MODEL",
       "qwen/qwen3.8-27b"
    ),
    max_completion_tokens=1000,
    messages=[
        {
            "role": "system",
            "content": "You are a helpful medical assistant. Give general information only and advise consulting a healthcare professional for diagnosis."
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Analyze this skin image and describe what you observe."
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{image_data}"
                    }
                }
            ]
        }
    ]
)

print(response.choices[0].message.content)"""