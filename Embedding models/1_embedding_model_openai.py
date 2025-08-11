from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    # With the `text-embedding-3` class
    # of models, you can specify the size
    # of the embeddings you want returned.
    dimensions=32
)

single_vector = embeddings.embed_query("What is the capital of Islamabad")
print(str(single_vector)[:100])  # Show the first 100 characters of the vector


document=[
    "What is the capital of Pakistan?",
    "What is the largest city in Pakistan?",
    "What is the official language of Pakistan?"
]

document_vectors = embeddings.embed_documents(document)
