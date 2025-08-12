from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Option 1: Using OpenRouter with LangChain (recommended)
model = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),  # Using environment variable for security
    model_name="openai/gpt-oss-20b:free"
)

# Use the invoke method to get a response
result = model.invoke("What is the capital of pakistan?")
print("Chat Model Result:", result.content)  # Output the result of the chat model invocation

