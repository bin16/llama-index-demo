import chromadb

from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

# 0. embedding model
embed_model = OllamaEmbedding(model_name="nomic-embed-text:latest")

# 1. Read content from data/
documents = SimpleDirectoryReader("./data/").load_data()

# 2. Vector Store - Open Database
db = chromadb.PersistentClient(path="test.db")
chroma_collection = db.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 3. Save to Disk
index = VectorStoreIndex.from_documents(
  documents,
  storage_context=storage_context,
  embed_model=embed_model,
)
