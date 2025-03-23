import os
from dotenv import load_dotenv

load_dotenv()
hf_token = os.getenv("HUGGINGFACE_TOKEN")

if hf_token:
    print("Hugging Face token loaded successfully.")
else:
    print("No token found.")
