# LLaMA 3 on NVIDIA GPUs via Docker

This is a program to run Meta's LLaMA 3 model on Docker using NVIDIA GPUs.

## Prerequisites

1. **Request access to LLaMA 3 from Meta**  
   Apply for access to the LLaMA 3 model via Meta's official site:  
   [Meta LLaMA 3](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)

2. **Generate Hugging Face Token**  
   You will need to issue a token from Hugging Face to access the model.  
   Detailed instructions can be found in the following article:  
   [How to Get Hugging Face Token](https://zenn.dev/shibayan/articles/b8a91a1c175685)

## Usage

### Modifying `llama3_script.py`

1. **Set Your Hugging Face Token**  
   In `llama3_script.py`, replace `'your_access_token'` in the `login(token='your_access_token')` function with your Hugging Face token.

2. **Specify the Input Prompt**  
   Modify the `prompt` in `llama3_script.py` to input the text you want the LLaMA model to process. Example:  
   ```python
   prompt = "Explain about Large Language Model briefly."
   ```

### Docker Commands

1. **Build Docker Image**  
   To build the Docker image, run the following command:
   ```bash
   docker image build -t llama3_7b:latest .
   ```

2. **Create Docker Container**  
   To create a container with GPU support, use the following command:
   ```bash
   docker container run -it --gpus all --name llama3_7b -v $(pwd)/src:/app llama3_7b:latest
   ```

3. **Start Docker Container**  
   If the container has already been created, start it with:
   ```bash
   docker start -i llama3_7b
   ```

4. **Run `llama3_script.py` on Docker**  
   To run the `llama3_script.py` inside the container, use:
   ```bash
   python3 llama3_script.py
   ```
   The first time you run the script, LLaMA-8B will be downloaded and inference will be performed. On subsequent executions, the model will not be downloaded again, and inference will proceed directly.

--- 

This format improves readability, ensures clarity for users, and provides step-by-step guidance.






# NVIDIA GPU上でLLaMA 3をDockerで動作させる

このプログラムは、NVIDIA GPUを使用してMeta社のLLaMA 3モデルをDocker上で動作させるためのものです。

## 事前準備

1. **Meta社からLLaMA 3の利用申請を行う**  
   Metaの公式サイトからLLaMA 3モデルの利用申請を行ってください。  
   [Meta LLaMA 3](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)

2. **Hugging Faceのトークンを発行する**  
   モデルにアクセスするために、Hugging Faceからトークンを発行する必要があります。  
   詳細な手順は、以下の記事を参考にしてください。  
   [Hugging Faceトークンの発行方法](https://zenn.dev/shibayan/articles/b8a91a1c175685)

## 使用方法

### `llama3_script.py` の設定

1. **Hugging Faceトークンを設定する**  
   `llama3_script.py`内の `login(token='your_access_token')` に、発行したHugging Faceのトークンを設定してください。

2. **入力プロンプトの設定**  
   `llama3_script.py`内の `prompt` 変数に、LLaMAモデルに入力するテキストを設定します。例：  
   ```python
   prompt = "大規模言語モデルについて簡単に説明してください。"
   ```

### Dockerコマンド

1. **Dockerイメージの作成**  
   以下のコマンドでDockerイメージを作成します：
   ```bash
   docker image build -t llama3_7b:latest .
   ```

2. **Dockerコンテナの作成**  
   以下のコマンドでGPUを使用してコンテナを作成します：
   ```bash
   docker container run -it --g

