import os
import anthropic
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Read API key
api_key = os.getenv("MINIMAX_API_KEY")

# Check if API key exists
if not api_key:
    raise ValueError(
        "MINIMAX_API_KEY not found. Add it to your .env file."
    )

# Create MiniMax client
client = anthropic.Anthropic(
    api_key=api_key,
    base_url="https://api.minimax.io/anthropic"
)

# Send a message
response = client.messages.create(
    model="MiniMax-M3",
    max_tokens=100,
    messages=[
        {
            "role": "user",
            "content": "Hello, what can you help me with?"
        }
    ]
)

# Print response
print(response.content[0].text)