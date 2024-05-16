# commands to run 
python3 ./convert-llama-ggml-to-gguf.py --input /Users/vaibhavsatpathy/Documents/pocs/genai_tests/models/llama-2-13b-chat.ggmlv3.q4_0.bin --output models/openorca-platypus2-13b.gguf.q4_0.bin

# GGMl file format link - 13b
https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/tree/main

# GGUF File fomrat link - 13b
https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/tree/main

# Steps for Llama3
1. Download the HF version of Llama3 and not the native version of .pth as that is not supported by llama.cpp for conversion.
2. Run the following command where you give the directory of where the model is store - python3 convert-hf-to-gguf.py /Users/vaibhavsatpathy/Documents/products/llama3/Meta-Llama-3-8B-HF --outtype q8_0
3. You can run python3 convert-hf-to-gguf.py --help to see the supported output types and other variables
4. The file is converted to .gguf format and stored in the same directory which we can use for execution.
5. To further quantize the model run - ./quantize /Users/vaibhavsatpathy/Documents/pocs/genai_tests/models/llama-3-8B/ggml-model-f16.gguf /Users/vaibhavsatpathy/Documents/pocs/genai_tests/models/llama-3-8B/ggml-model-q4_0.gguf Q4_0
6. Here you have to give the input ggup file that you want to quatize along with the path to where to store it and as the final variable the algorithm for quantization
7. The final file is ready to use and you are good to go for embeddings or chat using llama cpp.

# Notes - 
1. Have all the following packages installed - 
    - torch
    - torchvision
    - tensorflow
    - transformers (of HF)
    - llama-cpp-python
2. Refer this link of langchain for using it with llama app - https://python.langchain.com/v0.1/docs/integrations/providers/llamacpp/
3. Refer this for usage of Llama cpp with langchain - https://python.langchain.com/v0.1/docs/integrations/llms/llamacpp/
4. Refer this for Llama cpp github - https://github.com/ggerganov/llama.cpp?tab=readme-ov-file
5. You will need to clone the llama cpp repo and perform the make process so that you can install the pip version and use other sub functionalities like conversion and quantization.
6. Refer this on how to use Llama cpp python package for development and consumption of the ggup files - https://github.com/abetlen/llama-cpp-python
7. Refer this for Llama 3 github repo - https://github.com/meta-llama/llama3
8. Llama2 GGuF file links - https://huggingface.co/TheBloke/Llama-2-13B-chat-GGUF/tree/main
9. LLama2 GGML file links - https://huggingface.co/TheBloke/Llama-2-13B-chat-GGML/tree/main
10. Llama3 HF 8b files - https://huggingface.co/meta-llama/Meta-Llama-3-8B/tree/main
11. Llama3 HF 70b files - https://huggingface.co/meta-llama/Meta-Llama-3-70B/tree/main
12. Llama2 for Mac medium article - https://medium.com/@auslei/llama-2-for-mac-m1-ed67bbd9a0c2
