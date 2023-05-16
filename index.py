import os
import openai
from dotenv import load_dotenv
load_dotenv()

# LineBot 服務跑不動可能是 Webhook url 沒更新，記得更新 Webhook url 並 verify 取得 success 狀態
from flask import Flask, request, abort
from flask_ngrok import run_with_ngrok # import ngrok

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)



app = Flask(__name__)
run_with_ngrok(app) # run with ngrok

line_bot_api = LineBotApi(os.getenv('LINE_Channel_access_token')) # Channel access token
handler = WebhookHandler(os.getenv('LINE_Channel_Secret')) # Channel Secret


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=aoai(event.message.text))) # 把前面所建 askchatgpt 函式帶入回應即可


if __name__ == "__main__":
    app.run()