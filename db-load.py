import chromadb

from llama_index.core import StorageContext, VectorStoreIndex, Settings
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

# 0. LLM
Settings.llm = Ollama(model="deepseek-r1:latest", request_timeout=360.0)

# 0. Embedding Model
embed_model = OllamaEmbedding(model_name="nomic-embed-text:latest")

# 1. Vector Store - Open Database
db = chromadb.PersistentClient(path="test.db")
chroma_collection = db.get_or_create_collection("quickstart")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# 2. Read from DB
index = VectorStoreIndex.from_vector_store(
  vector_store,
  embed_model,
)

# 3. Query
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")
print(response)
