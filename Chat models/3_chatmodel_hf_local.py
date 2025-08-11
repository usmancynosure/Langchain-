from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv
import os

# create the hugging face pipline 
load_dotenv()

llm= HuggingFacePipeline.from_model_id(

    model_id="huggingfaceh4/zephyr-7b-beta",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.1,
        max_new_tokens=10

    )
)

model = ChatHuggingFace(llm=llm)
result=model.invoke("What is the capital of Pakistan?")  # Example usage

print("Chat Model Result:", result.content)  # Output the result of the chat model invocation   
