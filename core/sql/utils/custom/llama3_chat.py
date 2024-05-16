from llama_cpp import Llama

model_dict = {
    "llama_2_13b":"llama-2-13b/llama-2-13b-chat.gguf.q4_0.bin",
    "llama_3_8b": "llama-3-8B/ggml-model-q4_0.gguf",
    }
llm = Llama(
      model_path=f"/app/models/{model_dict.get('llama_3_8b')}",
      # n_gpu_layers=-1, # Uncomment to use GPU acceleration
      seed=1337, # Uncomment to set a specific seed
      # n_ctx=2048, # Uncomment to increase the context window
)


def chat_response(text: str):
    output = llm(
        f"Q: {text} A: ", # Prompt
        max_tokens=2000, # Generate up to 32 tokens, set to None to generate up to the end of the context window
        stop=["Q:", "\n"], # Stop generating just before the model would generate a new question
        echo=True # Echo the prompt back in the output
    ) # Generate a completion, can also call create_completion
    return output