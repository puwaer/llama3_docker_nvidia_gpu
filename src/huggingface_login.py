# 自分のHuggingFaceアカウントと紐付ける(申請済みのアカウントでないとモデルをダウンロードできないため)、terminalの場合はhuggingface-cli loginを実行してください。
from huggingface_hub import login
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, BitsAndBytesConfig

# https://huggingface.co/meta-llama/Meta-Llama-3-8B
# https://huggingface.co/meta-llama/Meta-Llama-3-8B/tree/main
# from_pretrainedの引数にモデル名を指定すると、モデルをダウンロードしてきてくれます。ダウンロードには3分ほどかかります。

login(token='your_access_token')
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Meta-Llama-3-8B")