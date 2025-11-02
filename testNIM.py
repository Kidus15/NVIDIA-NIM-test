# testNIM.py
import os
import sys
from openai import OpenAI

# === 1) Insert your NVIDIA API key ===
NVIDIA_API_KEY = "api_key here"  # <-- USE YOUR NEW KEY (after revoking the old one!)

# === 2) Try a different model that's commonly available ===
MODEL = "meta/llama-3.1-8b-instruct"  # This model is widely available on NVIDIA's platform

# === 3) Create the client ===
client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1", # a base url is a url that points to the NVIDIA NIM API endpoints
    api_key=NVIDIA_API_KEY,
)


prompt = "How do I acieve a good credit score?"
# === 4) Make a simple chat request ===
messages = [
    {"role": "user", "content": prompt}
]




try:
    resp = client.chat.completions.create(
        model=MODEL,
        messages=messages,
        max_tokens=120,
        temperature=0.7,
    )

    print("\n=== MODEL RESPONSE ===\n")
    print(resp.choices[0].message.content.strip())

except Exception as e:
    print("\n=== REQUEST FAILED ===")
    print(e)
