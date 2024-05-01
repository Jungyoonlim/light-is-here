import json
from sentence_transformers import SentenceTransformer

# Load the pre-trained Korean language model
model = SentenceTransformer('sentence-transformers/xlm-r-large-en-ko-nli-ststb')

# Load the JSON files
json_files = ['part1_data.json', 'part2_data.json', 'part3_data.json', 'part4_data.json']

# Create an empty list to store the embeddings
embeddings_data = []

# Generate embeddings for each JSON file
for file in json_files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            title = item['title']
            content = item['content']
            # Generate embedding for the content
            embedding = model.encode(content).tolist()
            # Append the embedding data to the list
            embeddings_data.append({
                'title': title,
                'embedding': embedding
            })

# Save the embeddings data to a JSON file
with open('embeddings.json', 'w', encoding='utf-8') as f:
    json.dump(embeddings_data, f, ensure_ascii=False, indent=4)

print("Embeddings generated and saved to embeddings.json")