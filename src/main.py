from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
from pydub import AudioSegment
from pydub.playback import play
import io
from dotenv import load_dotenv
import os

# .envから環境変数をロード
load_dotenv()

# OpenAIのクライアントを作成
client = OpenAI()

app = FastAPI()


class Text(BaseModel):
    text: str


@app.post("/stream_and_play/")
async def stream_and_play(text: Text):
    # OpenAIの音声生成APIを呼び出し、結果を取得します
    response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=text.text,
    )

    # バイナリ形式のレスポンス内容をバイトストリームに変換します
    byte_stream = io.BytesIO(response.content)

    # バイトストリームからオーディオデータを読み込みます
    audio = AudioSegment.from_file(byte_stream, format="mp3")

    # オーディオを再生します
    play(audio)

    # オーディオデータをファイルに書き込みます
    audio.export("output.mp3", format="mp3")

    # 成功メッセージを返します
    return {"message": "音声の再生と保存が成功しました"}
