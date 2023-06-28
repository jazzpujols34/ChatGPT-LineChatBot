from flask import Flask, request, abort
import os
import openai
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

openai.api_type = "azure"
openai.api_version = "2023-06-01-preview"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = os.getenv("OPENAI_API_BASE")

app = Flask(__name__)

def aoai(q):
    msg = ""
    prompt_text = (
        "The following is a conversation with an AI assistant. "
        "The assistant is helpful, creative, clever, and very friendly. \n"
        "\nHuman: Hello, who are you? \n"
        "AI: Hello, I am an AI assistant. I am here to help you with anything you need. "
    )
    response_az = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_text + q,
        temperature=1,
        max_tokens=200,
        top_p=0.5,
        frequency_penalty=0,
        presence_penalty=0,
        best_of=1,
        stop=None
    )
    msg += (response_az['choices'][0]['text'].strip())
    return msg


line_bot_api = LineBotApi(os.getenv('LINE_ACCESS_TOKEN'))
handler1 = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))

@app.route("/")
def saturday():
    return 'It\'s finally Saturday!!!'

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler1.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)
    return 'OK'

@handler1.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=aoai(event.message.text))
    )

if __name__ == "__main__":
    app.run()
