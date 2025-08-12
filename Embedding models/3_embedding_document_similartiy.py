from langchain_openai import EmbeddingOpenAI
from dotenv import load_dotenv
from scikit.metrics.pairwise import cosine_similarity


load_dotenv()

embedding = EmbeddingOpenAI(
    model="text-embedding-3-large",
    dimensions=32
)

document = [
    "What is the capital of Pakistan?",
    "What is the largest city in Pakistan?",
    "What is the official language of Pakistan?"
]

document_vectors = embedding.embed_documents(document)

# single vector
single_vector = embedding.embed_query("What is the capital of Pakistan?")

scores = cosine_similarity([single_vector], document_vectors)[0] 

# make the enumerate function and all function in the list 

# sort on the second argument [0,0.8484]
index, score=sorted(list(enumerate(scores)), key=lambda x: x[1])[-1]


print(document[index])
print("Cosine Similarity Score:", score)