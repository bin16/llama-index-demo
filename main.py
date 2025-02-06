# https://docs.llamaindex.ai/en/stable/getting_started/starter_example_local/
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

from settings.model import init_models

init_models()

# 1. Read context from local files in data/ directory
documents = SimpleDirectoryReader("data").load_data()

# 2. Index
index = VectorStoreIndex.from_documents(documents)

# 3. Query
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")

print(response)
