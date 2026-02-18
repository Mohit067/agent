import os
from dotenv import load_dotenv
from google.adk.models.lite_llm import LiteLlm

load_dotenv()

MODEL = LiteLlm(
    model="groq/openai/gpt-oss-20b"
)
