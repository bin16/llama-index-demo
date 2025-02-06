### Installation

It is recommended to setup virtualenv before install packages.

https://docs.llamaindex.ai/en/stable/getting_started/installation/


```sh
# install necessary packages
pip install -r requirements.txt
```

### Download Models

```sh
ollama pull llama3.2:latest
ollama pull nomic-embed-text:latest
```

### Files

- main.py - read context from files, and query
- db-save.py - read context from files, and write to chrome db
- db-load.py - read context from chroma db, and query
- settings
  - chroma.py - init chroma db and return vector_store
  - model.py - init LLM and embeddings models

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
