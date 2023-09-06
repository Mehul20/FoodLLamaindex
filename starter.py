from pathlib import Path
from llama_index import VectorStoreIndex, download_loader
from dotenv import load_dotenv
import os
import openai

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

if openai_api_key is None:
    raise ValueError("OpenAI API key not found.")

openai.api_key = openai_api_key

SimpleCSVReader = download_loader("SimpleCSVReader")

loader = SimpleCSVReader(encoding="utf-8")
documents = loader.load_data(file=Path('./restaurants.csv'))

index = VectorStoreIndex.from_documents(documents)
query_engine = index.as_query_engine()
response = query_engine.query("Some Italian Restaurants In Atlanta?")
print(response)