import os
import openai
from dotenv import load_dotenv
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

load_dotenv()

openai.api_type = "azure"
openai.api_version = "2022-12-01"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('LINE_Channel_access_token'))
handler = WebhookHandler(os.getenv('LINE_Channel_Secret'))

@app.route("/", methods=['GET'])
def home():
    return 'Hello, this is my LINE chatbot!'

def aoai(q):
    msg = ""
    response_az = openai.Completion.create(
        engine="text-davinci-003",
        prompt=q,
        temperature=1,
        max_tokens=300,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None
    )
    msg += (response_az['choices'][0]['text'].strip())
    return msg

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
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
        TextSendMessage(text=aoai(event.message.text))
    )

if __name__ == "__main__":
    app.run()
