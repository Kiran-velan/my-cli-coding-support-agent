from litellm import completion
import os
from dotenv import load_dotenv

load_dotenv()

MODEL = os.getenv("MODEL", "gemini/gemini-2.5-flash")

def chat_completion(messages, tools):
    return completion(
        model=MODEL,
        messages=messages,
        tools=tools,
    )