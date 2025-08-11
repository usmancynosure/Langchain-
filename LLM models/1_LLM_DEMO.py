from langchain_openai import OpenAI

from dotenv import load_dotenv
import os
load_dotenv()


llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

result= llm.invoke("What is the capital of France?")  # Example usage

print("LLM Result:", result)  # Output the result of the LLM invocation