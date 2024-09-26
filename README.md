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






以下は日本語のREADMEです。

---

# NVIDIA GPU上でLLaMA 3をDockerで動作させる

このプログラムは、NVIDIA GPUを使用してMeta社のLLaMA 3モデルをDocker上で動作させるためのものです。

## 前提条件

1. **Meta社からLLaMA 3の利用申請を行う**  
   Meta社の公式サイトからLLaMA 3モデルの利用申請を行ってください。  
   [Meta LLaMA 3](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)

2. **Hugging Faceのトークンを発行する**  
   モデルにアクセスするために、Hugging Faceからトークンを発行する必要があります。  
   詳細な手順は以下の記事を参照してください。  
   [Hugging Faceトークンの発行方法](https://zenn.dev/shibayan/articles/b8a91a1c175685)

## 使い方

### `llama3_script.py`の修正

1. **Hugging Faceトークンを設定する**  
   `llama3_script.py`の `login(token='your_access_token')` に、発行したHugging Faceトークンを設定してください。

2. **入力プロンプトを設定する**  
   `llama3_script.py`内の `prompt` を修正し、LLaMAモデルに入力するテキストを設定します。例：  
   ```python
   prompt = "大規模言語モデルについて簡単に説明してください。"
   ```

### Dockerコマンド

1. **Dockerイメージを作成する**  
   以下のコマンドを実行して、Dockerイメージをビルドします。
   ```bash
   docker image build -t llama3_7b:latest .
   ```

2. **Dockerコンテナを作成する**  
   以下のコマンドを実行して、GPU対応のDockerコンテナを作成します。
   ```bash
   docker container run -it --gpus all --name llama3_7b -v $(pwd)/src:/app llama3_7b:latest
   ```

3. **Dockerコンテナを起動する**  
   コンテナが既に作成されている場合、以下のコマンドでコンテナを起動します。
   ```bash
   docker start -i llama3_7b
   ```

4. **コンテナ内で`llama3_script.py`を実行する**  
   コンテナ内で`llama3_script.py`を実行するには、以下のコマンドを使用します。
   ```bash
   python3 llama3_script.py
   ```
   スクリプトを初めて実行すると、LLaMA-8Bモデルがダウンロードされ、推論が行われます。2回目以降の実行時にはダウンロードは行われず、推論のみが行われます。
