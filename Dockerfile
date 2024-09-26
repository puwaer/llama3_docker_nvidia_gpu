# ベースイメージとして Ubuntu を使用
#FROM ubuntu:20.04
# ベースイメージとして NVIDIA CUDA ベースの Python 3 イメージを使用
FROM nvidia/cuda:11.3.1-cudnn8-runtime-ubuntu20.04

# 必要な依存ライブラリをインストール
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    git \
    && rm -rf /var/lib/apt/lists/*

# 作業ディレクトリを設定
WORKDIR /app

# 必要な Python ライブラリをインストール
COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
RUN pip3 install -U transformers huggingface_hub
RUN pip3 install -U bitsandbytes 
RUN pip3 install -U accelerate


# スクリプトファイルをコピー
COPY /src/huggingface_login.py /app/
COPY /src/llama3_script.py /app/

# LLaMA3 の実行コマンド
#CMD ["python3", "your_llama3_script.py"]
CMD ["/bin/bash"]

