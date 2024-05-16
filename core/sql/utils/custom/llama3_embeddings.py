from llama_cpp import Llama

model_dict = {
    "llama_2_13b":"llama-2-13b/llama-2-13b-chat.gguf.q4_0.bin",
    "llama_3_8b": "llama-3-8B/ggml-model-q4_0.gguf",
    }
llm = Llama(
      model_path=f"/app/models/{model_dict.get('llama_3_8b')}",
      embedding=True,
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
)


def create_embeddings(text: str):
    embeddings = llm.create_embedding(text)
    return embeddings
