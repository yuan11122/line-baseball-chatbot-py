#
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

from full import *

app = Flask(__name__)

import os
from dotenv import load_dotenv
load_dotenv()

Line_access_token = os.getenv("LINE_ACCESS_TOKEN")
Line_secret_key = os.getenv("LINE_SECRET_KEY")

line_bot_api = LineBotApi(Line_access_token)
handler = WebhookHandler(Line_secret_key)

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    print(body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'



@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = event.message.text

    if '選單' in message_text or '棒球Menu' in message_text:
        message = button_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '職業比賽' in message_text and message_text != '我想了解國內的職業比賽':
        message = Image_Carousel_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '國際比賽' in message_text and message_text != '我想了解臺灣的國際比賽':
        message = Carousel_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '黑豹旗' in message_text and message_text != '我想了解黑豹旗':
        message = Flex_Message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '棒球場' in message_text and message_text != '我想了解臺灣的棒球場':
        message = Flex_Message1()
        line_bot_api.reply_message(event.reply_token, message)
    # else:
    #      line_bot_api.reply_message(
    #          event.reply_token,
    #          TextSendMessage(text='關鍵字請打對，謝謝^_^'))    

@handler.add(PostbackEvent)
def handle_postback(event):
    data = event.postback.data
    userID = event.source.user_id
    if data == '國內職業比賽':
        messages = Image_Carousel_message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)
    
    elif data == '國際比賽':
        messages = Carousel_Template()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)
    
    elif data == '學生棒球':
        messages = Flex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '棒球場':
        messages = Flex_Message1()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)
        
if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
    #app.run(debug=True)
