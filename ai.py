from prompt import PROMPT
from google import genai
import os

GEMINI = os.environ.get('GEMINIKEY')
MODEL = os.environ.get('GEMINIMODEL')

def gemini_ai():
    client = genai.Client(api_key=f'{GEMINI}')
    chat = client.chats.create(model=f'{MODEL}', history=[])
    chat.send_message(PROMPT)
    return chat