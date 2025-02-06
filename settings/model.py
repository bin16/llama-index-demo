from llama_index.core import Settings

from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

def init_models():
  Settings.embed_model = OllamaEmbedding(model_name="nomic-embed-text:latest")
  Settings.llm = Ollama(model="llama3.2:latest", request_timeout=360.0)
