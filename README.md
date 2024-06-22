# chat tts

- <https://chattts.com/zh>
- https://github.com/2noise/ChatTTS/blob/main/docs/cn/README.md

```sh
(base) han@alienware:/mnt/d/coding$ which python
/home/han/anaconda3/bin/python
python -m pip install --upgrade pip
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

```sh
conda create -n tts_env python=3.11
conda activate tts_env
which python

# /home/han/anaconda3/envs/tts_env/bin/python
# D:\garden\anaconda3\envs\tts_env
```

```sh
git clone https://github.com/2noise/ChatTTS
cd ChatTTS
# sudo apt install gcc
# sudo apt install git-lfs
# gcc --version
# conda install -c conda-forge pyproject2conda
pip install -r requirements.txt
```

```sh
git lfs install
git clone https://www.modelscope.cn/pzc163/chatTTS.git pzc163_chatTTS
# git clone https://huggingface.co/2Noise/ChatTTS HF_ChatTTS
```

```sh
cp /mnt/d/coding/hello-chat-tts/hello_tts.py /mnt/d/coding/ChatTTS/
python /mnt/d/coding/ChatTTS/hello_tts.py
```

```sh
pip uninstall torch torchvision torchaudio -y
pip install torch==2.1.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu121 --proxy http://localhost:57885
```

Traceback (most recent call last):
  File "/mnt/d/coding/ChatTTS/hello_tts.py", line 9, in <module>
    chat.load_models(compile=True,source='local', local_path=modelPath)
  File "/mnt/d/coding/ChatTTS/ChatTTS/core.py", line 59, in load_models
    if not check_all_assets(update=True):
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/mnt/d/coding/ChatTTS/ChatTTS/utils/download.py", line 61, in check_all_assets
    current_dir, model, os.environ[f"sha256_asset_{menv}"], update
                        ~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen os>", line 679, in __getitem__
KeyError: 'sha256_asset_Decoder_pt'
