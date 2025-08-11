from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model=ChatOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="gpt-4"
)

# //use the invoke method to get a response
result = model.invoke("Hello, how are you?")
print("Chat Model Result:", result.content)  # Output the result of the chat model invocation

