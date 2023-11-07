## OpenAI TTS StreamingのバックエンドAPI

OpenAIのTTS Streamingを試してみたかったので、FastAPIを使って簡易的に試してみた。UIを持って出力するならばNext.jsとかを使うのが良いのかも。


### 実行手順

1. `.env.example`をコピーして`.env`を作成します。
2. `.env`に`OPENAI_API_KEY`を記載します。
3. `make install`を実行します。
4. `make run`を実行するとAPIが立ち上がります。
5. Swaggerから[`stream_and_play`エンドポイント](http://127.0.0.1:8000/docs#/default/stream_and_play_stream_and_play__post)を確認します。
6. `stream_and_play`エンドポイントの`text`フィールドの値を変えることで、streamingで受け取る音声データを再生することができます。


