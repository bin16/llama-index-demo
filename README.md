## Installation

https://docs.llamaindex.ai/en/stable/getting_started/installation/

```sh
pip install -r requirements.txt
```

## python main.py

read files under data/ as context and answer question.

----

### LLM

#### Ollama

```py
from llama_index.core import Settings
from llama_index.llms.ollama import Ollama

Settings.llm = Ollama(model="llama3.2:latest", request_timeout=360.0)
```

### Embedding Model

#### Ollama

```py
from llama_index.core import Settings
from llama_index.embeddings.ollama import OllamaEmbedding

Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text:latest")
```

### Vector Store

all: https://docs.llamaindex.ai/en/stable/module_guides/storing/vector_stores/

#### ChromaDB

https://docs.llamaindex.ai/en/stable/examples/vector_stores/ChromaIndexDemo/

#### Postgres

https://docs.llamaindex.ai/en/stable/examples/vector_stores/postgres/

#### Qdrand

https://docs.llamaindex.ai/en/stable/examples/vector_stores/QdrantIndexDemo/
