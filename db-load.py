from llama_index.core import StorageContext, VectorStoreIndex

from settings.models import init_models
from settings.chroma import init_chroma

init_models()

vector_store = init_chroma()

# 1. Read context from ChromaDB
# 2. Index
index = VectorStoreIndex.from_vector_store(
  vector_store,
)

# 3. Query
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")

print(response)
