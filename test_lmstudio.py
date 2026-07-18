import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url=os.getenv("LM_STUDIO_BASE_URL"),
    api_key=os.getenv("LM_STUDIO_API_KEY"),
)

response = client.chat.completions.create(
    model=os.getenv("LM_STUDIO_MODEL"),
    messages=[{"role": "user", "content": "Hola, ¿funcionas?"}],
)

print(response.choices[0].message.content)