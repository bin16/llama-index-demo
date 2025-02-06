import chromadb

from llama_index.core import SimpleDirectoryReader, StorageContext, VectorStoreIndex
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

from settings.models import init_models
from settings.chroma import init_chroma

init_models()

# 1. Read context from files in data/ directory
documents = SimpleDirectoryReader("./data/").load_data()

vector_store = init_chroma()
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 2. Index
# 3. Save to ChromaDB
index = VectorStoreIndex.from_documents(
  documents,
  storage_context=storage_context,
)
