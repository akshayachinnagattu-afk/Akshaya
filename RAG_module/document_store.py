from sentence_transformers import SentenceTranformers
import 

with open("fest_info.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(f"Your file has {len(text)} characters.")
print()
print("sample text:", text[:300])

def chunk_text(text,chunk_size = 300,overlap=50):
    chunks=[]
    start=0
    while start < len(text):
        chunks.append(text[start:start + chunk_size])
        start += chunk_size - overlap
    return chunks

chunks= chunk_text(text)

model = SentenceTranformers('all-miniLM-L6-V2')
embiddings = model.encode(chunks)


print(f"total {len(chunks)}created -> shape of embeddings: {embiddings.shape}")

for i in range(len(chunks)):
    print(f"chunk_{i+1}: {chunks[i]}")
    print()
    print("...............................................")

