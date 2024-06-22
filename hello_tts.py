import ChatTTS
from IPython.display import Audio
import torchaudio

# modelPath="/mnt/d/coding/pzc163_chatTTS"
modelPath="/mnt/d/coding/HF_ChatTTS"

chat = ChatTTS.Chat()
chat.load_models(compile=True,source='local', local_path=modelPath)

texts = ["你好 Chat TTS",]
wavs = chat.infer(texts, use_decoder=True)
torchaudio.save("output1.wav", torch.from_numpy(wavs[0]), 24000)