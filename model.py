from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
load_dotenv()
model=init_chat_model("gpt-oss:20b-cloud",
    model_provider="openai",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://ollama.com/v1"
)
