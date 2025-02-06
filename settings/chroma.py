import chromadb
from llama_index.vector_stores.chroma import ChromaVectorStore

def init_chroma() -> ChromaVectorStore:
  db = chromadb.PersistentClient(path="test.db")
  chroma_collection = db.get_or_create_collection("quickstart")
  vector_store = ChromaVectorStore(chroma_collection=chroma_collection)

  return vector_store
