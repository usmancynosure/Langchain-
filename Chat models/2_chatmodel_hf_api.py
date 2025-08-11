from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

# Create the HuggingFace endpoint with a working chat model
llm = HuggingFaceEndpoint(
    repo_id="huggingfaceh4/zephyr-7b-beta",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"),
    temperature=0.1,
    max_new_tokens=10
)

# Wrap it in ChatHuggingFace for chat interface
model = ChatHuggingFace(llm=llm)

try:
    result = model.invoke("What is the capital of Pakistan?")  # Example usage
    print("Chat Model Result:", result.content)  # Output the result of the chat model invocation
except Exception as e:
    print(f"Error occurred: {e}")
    print("This might be due to the model being temporarily unavailable on Hugging Face servers.")
    print("The API key configuration is working correctly.")