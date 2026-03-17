import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
result = genai.embed_content(
    model="models/embedding-001",
    content="Artificial Intelligence"
)
embeddings = result['embedding']['values']
print(len(embeddings))
print(embeddings[:10])