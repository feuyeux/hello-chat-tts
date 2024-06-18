import ChatTTS
from IPython.display import Audio
import torchaudio

modelPath="D:\coding\hello-chat-tts\pzc163_chatTTS"
chat = ChatTTS.Chat()
chat.load_models(compile=False,source='local', local_path=modelPath)

texts = ["你好 Chat TTS",]
wavs = chat.infer(texts, use_decoder=True)
torchaudio.save("output1.wav", torch.from_numpy(wavs[0]), 24000)