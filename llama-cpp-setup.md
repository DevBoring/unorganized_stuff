https://github.com/ggml-org/llama.cpp/releases

windows x64 CUDA + CUDA dlls

主檔案解壓縮丟新創資料夾`C:\llama-cpp`

dlls解壓縮同樣丟`C:\llama-cpp`

載需要的gguf檔models丟新創資料夾`C:\llama-cpp\models`

在`C:\llama-cpp`創`models.ini` (底下自己改)

```ini
version = 1

[*]
n-gpu-layers = 99          ; 盡量用 GPU
ctx-size = 4096            ; 上下文大小
flash-attn = 1             ; 開Flash Attention
cache-type-k = q8_0        ; KV Cache 用 8-bit
cache-type-v = q8_0

[gemma-4-26B]
model = ./models/gemma-4-26B-A4B-it-UD-IQ3_XXS.gguf
alias = gemma-4-26B

[qwen3.6-35B]
model = ./models/Qwen3.6-35B-A3B-UD-Q2_K_XL.gguf
alias = qwen3.6-35B

[bonsai-27B]
model = ./models/Ternary-Bonsai-27B-Q2_0.gguf
alias = bonsai-27B
```

終端機執行

```powershell
cd C:\llama-cpp
.\llama-server.exe --models-preset ./models.ini
```

