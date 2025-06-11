import chromadb

try:
    client = chromadb.Client()
    collection = client.create_collection("test")
    print("ChromaDB basic test passed!")
except Exception as e:
    print(f"ChromaDB basic test failed: {e}")