from huggingface_hub import login
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig
import os

# HuggingFace のトークンでログイン
login(token='your_access_token')

# モデルとトークナイザーの名前
model_name = "meta-llama/Meta-Llama-3-8B"

# キャッシュディレクトリのパス
cache_dir = os.path.join(os.path.expanduser("~"), ".cache", "huggingface")

# トークナイザーをロード
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=cache_dir)

# メモリが足りない場合の量子化設定
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_compute_dtype=torch.float16,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_use_double_quant=False,
)

# モデルをロード
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    quantization_config=bnb_config,
    torch_dtype=torch.bfloat16,
    cache_dir=cache_dir
)

# プロンプト
prompt = "Explain about Large Language Model briefly."
#prompt = "大規模言語について教えて"


# モデル入力の準備
model_input = tokenizer(prompt, return_tensors="pt").to(model.device)
input_ids = model_input["input_ids"]

# 推論を実行
with torch.no_grad():
    result = model.generate(
        input_ids,
        max_new_tokens=300,
        do_sample=False,  # Temperature を有効にする場合は True にしてください。
        # temperature=0.6,
        # top_p=0.9
    )
    result = result[0][input_ids.shape[-1]:]
    output = tokenizer.decode(result, skip_special_tokens=True)
    print("\n-----生成結果-----\n", output)

# メモリの解放
del input_ids
del model_input
torch.cuda.empty_cache()
