# chat tts

- <https://chattts.com/zh>
- <https://github.com/2noise/ChatTTS/blob/main/README_CN.md>


```sh
# D:\garden\anaconda3\envs\tts_env
conda create -n tts_env python=3.11
conda activate tts_env
git clone https://github.com/2noise/ChatTTS
cd ChatTTS
pip install Cython
conda install -c conda-forge pynini=2.1.5y
pip install -r requirements.txt

pip uninstall torch torchvision torchaudio -y
pip install torch==2.1.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu121
```

```sh
git lfs install
git clone https://www.modelscope.cn/pzc163/chatTTS.git pzc163_chatTTS
git clone https://huggingface.co/2Noise/ChatTTS HF_ChatTTS
```

```sh
# cd ChatTTS
conda activate tts_env
cp ../hello_tts.py .
python hello_tts.py
```
