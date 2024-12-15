# chat tts

- <https://chattts.com/zh>
- https://github.com/2noise/ChatTTS/blob/main/docs/cn/README.md

预备备

```sh
(base) han@alienware:/mnt/d/coding$ which python
/home/han/anaconda3/bin/python
python -m pip install --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

创建ChatTTS的conda环境

```sh
conda create -n tts_env python=3.11
conda activate tts_env
which python

# WSL: /home/han/anaconda3/envs/tts_env
# Windows: D:\garden\anaconda3\envs\tts_env
```

下载ChatTTS代码并安装依赖

```sh
cd /mnt/d/coding
git clone https://github.com/2noise/ChatTTS
cd ChatTTS
# sudo apt install gcc
# sudo apt install git-lfs
# gcc --version
# conda install -c conda-forge pyproject2conda
pip install -r requirements.txt
pip uninstall torch torchvision torchaudio -y
pip install torch==2.1.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu121
```

运行示例

```sh
cp /mnt/d/coding/hello-chat-tts/hello_tts.py /mnt/d/coding/ChatTTS/
python /mnt/d/coding/ChatTTS/hello_tts.py
```

(可选)本地模式

```sh
cd /mnt/d/coding
git lfs install
# 魔塔
git clone https://www.modelscope.cn/pzc163/chatTTS.git pzc163_chatTTS
# 抱抱脸
git clone https://huggingface.co/2Noise/ChatTTS HF_ChatTTS
```

```python
pzc163_chatTTS = "/mnt/d/coding/pzc163_chatTTS"
HF_ChatTTS = "/mnt/d/coding/HF_ChatTTS"
modelPath = pzc163_chatTTS

chat.load(
    source="local",
    custom_path=modelPath,
    compile=False,
    # device='cuda',
)
```