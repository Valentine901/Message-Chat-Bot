import os 
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")
API_URL = "https://api.groq.com/openai/v1/chat/completions"

if not API_KEY:
    raise RuntimeError("GROQ_API_KEY is missing. Check your .env file")