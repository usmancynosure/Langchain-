from langchain_openai import ChatOpenAI
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

print("=" * 60)
print("COMPARISON: LangChain vs Direct OpenAI Client with OpenRouter")
print("=" * 60)

# Method 1: Using LangChain with OpenRouter (Recommended for LangChain projects)
print("\n🔗 Method 1: LangChain ChatOpenAI with OpenRouter")
print("-" * 50)

try:
    langchain_model = ChatOpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        model_name="openai/gpt-oss-20b:free",
        temperature=0.7
    )
    
    langchain_result = langchain_model.invoke("What is the meaning of life?")
    print("LangChain Result:", langchain_result.content)
    
except Exception as e:
    print(f"LangChain Error: {e}")

print("\n" + "=" * 60)

# Method 2: Direct OpenAI Client with OpenRouter
print("\n🔧 Method 2: Direct OpenAI Client with OpenRouter")
print("-" * 50)

try:
    direct_client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=os.getenv("OPENROUTER_API_KEY")  # Using environment variable
    )
    
    direct_completion = direct_client.chat.completions.create(
        model="openai/gpt-oss-20b:free",
        messages=[
            {
                "role": "user",
                "content": "What is the meaning of life?"
            }
        ],
        temperature=0.7
    )
    
    print("Direct Client Result:", direct_completion.choices[0].message.content)
    
except Exception as e:
    print(f"Direct Client Error: {e}")

print("\n" + "=" * 60)
print("💡 Key Differences:")
print("   • LangChain: Better for complex workflows, chains, and agents")
print("   • Direct Client: More control, lower-level access")
print("   • Both: Support OpenRouter for access to multiple models")
print("=" * 60)
