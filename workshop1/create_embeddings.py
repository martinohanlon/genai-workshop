from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI

llm = OpenAI()

response = llm.embeddings.create(
        input="Text to create embeddings for",
        model="text-embedding-ada-002"
    )

print(response.data[0].embedding)