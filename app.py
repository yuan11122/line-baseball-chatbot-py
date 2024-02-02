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
from googlesheet import *

import pygsheets
import pandas as pd

print(cpbl)


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

@handler.add(FollowEvent)
def handle_follow_event(event):
    messages = follow()
    messages1 = main_message()
    message=[messages, messages1]
    line_bot_api.reply_message(event.reply_token, message)

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message_text = event.message.text

    if '選單' in message_text or '棒球Menu' in message_text:
        message = main_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '職業比賽' in message_text and message_text != '我想了解國內的職業比賽':
        message = Image_Carousel_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '國際比賽' in message_text and message_text != '我想了解臺灣的國際比賽':
        message = international_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '黑豹旗' in message_text and message_text != '我想了解黑豹旗':
        message = Flex_Message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '棒球場' in message_text and message_text != '我想了解臺灣的棒球場':
        message = Flex_Message1()
        line_bot_api.reply_message(event.reply_token, message)
    elif '中信兄弟' in message_text:
        message = brotherFlex_Message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '樂天桃猿' in message_text:
        message = monkeyFlex_Message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '統一獅' in message_text:
        message = lionFlex_Message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '富邦悍將' in message_text:
        message = fubonFlex_Message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '味全龍' in message_text:
        message = dragonFlex_Message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '台鋼雄鷹' in message_text:
        message = eagleFlex_Message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '棒球場' in message_text:
        message = Flex_Message1()
        line_bot_api.reply_message(event.reply_token, message)
    elif '球星' in message_text:
        message = player_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '敬請期待' in message_text:
        message = international_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我想了解國內的職業比賽' in message_text:
        message = Image_Carousel_message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我想了解臺灣的國際比賽' in message_text:
        message = international_Template()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我想了解黑豹旗' in message_text:
        message = Flex_Message()
        line_bot_api.reply_message(event.reply_token, message)
    elif '我想了解臺灣的棒球場' in message_text:
        message = Flex_Message1()
        line_bot_api.reply_message(event.reply_token, message)
    else:
          line_bot_api.reply_message(
              event.reply_token,
              TextSendMessage(text='關鍵字請打對，或是輸入「選單」或「棒球Menu」進行互動，謝謝^_^'))    

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
        messages = international_Template()
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
    
    elif data == '傳奇球星':
        messages = player_message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '中信兄弟賽程':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        final_date=event.postback.params['date']
        selected_rows = cpbl[(cpbl['日期無星期'] == final_date) & ((cpbl['主隊'] == '中信兄弟') | (cpbl['客隊'] == '中信兄弟'))]
        for _, row in selected_rows.iterrows():
            messages = cpblFlex_Message(row)
        reply_message = brotherFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '樂天桃猿賽程':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        final_date=event.postback.params['date']
        selected_rows = cpbl[(cpbl['日期無星期'] == final_date) & ((cpbl['主隊'] == '樂天桃猿') | (cpbl['客隊'] == '樂天桃猿'))]
        for _, row in selected_rows.iterrows():
            messages = cpblFlex_Message(row)
        reply_message = monkeyFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)
    
    elif data == '統一獅賽程':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        final_date=event.postback.params['date']
        selected_rows = cpbl[(cpbl['日期無星期'] == final_date) & ((cpbl['主隊'] == '統一獅') | (cpbl['客隊'] == '統一獅'))]
        for _, row in selected_rows.iterrows():
            messages = cpblFlex_Message(row)
        reply_message = lionFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '富邦悍將賽程':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        final_date=event.postback.params['date']
        selected_rows = cpbl[(cpbl['日期無星期'] == final_date) & ((cpbl['主隊'] == '富邦悍將') | (cpbl['客隊'] == '富邦悍將'))]
        for _, row in selected_rows.iterrows():
            messages = cpblFlex_Message(row)
        reply_message = fubonFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '味全龍賽程':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        final_date=event.postback.params['date']
        selected_rows = cpbl[(cpbl['日期無星期'] == final_date) & ((cpbl['主隊'] == '味全龍') | (cpbl['客隊'] == '味全龍'))]
        for _, row in selected_rows.iterrows():
            messages = cpblFlex_Message(row)
        reply_message = dragonFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '台鋼雄鷹賽程':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        final_date=event.postback.params['date']
        selected_rows = cpbl[(cpbl['日期無星期'] == final_date) & ((cpbl['主隊'] == '台鋼雄鷹') | (cpbl['客隊'] == '台鋼雄鷹'))]
        for _, row in selected_rows.iterrows():
            messages = cpblFlex_Message(row)
        reply_message = eagleFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '中信兄弟上半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = firststanding[(firststanding['球隊'] == '中信兄弟')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = brotherFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '中信兄弟下半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = laststanding[(laststanding['球隊'] == '中信兄弟')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = brotherFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '中信兄弟全年戰績':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = allstanding[(allstanding['球隊'] == '中信兄弟')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = brotherFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '樂天桃猿上半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = firststanding[(firststanding['球隊'] == '樂天桃猿')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = monkeyFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '樂天桃猿下半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = laststanding[(laststanding['球隊'] == '樂天桃猿')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = monkeyFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '樂天桃猿全年戰績':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = allstanding[(allstanding['球隊'] == '樂天桃猿')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = monkeyFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '統一獅上半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = firststanding[(firststanding['球隊'] == '統一獅')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = lionFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '統一獅下半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = laststanding[(laststanding['球隊'] == '統一獅')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = lionFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '統一獅全年戰績':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = allstanding[(allstanding['球隊'] == '統一獅')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = lionFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)
    
    elif data == '富邦悍將上半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = firststanding[(firststanding['球隊'] == '富邦悍將')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = fubonFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '富邦悍將下半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = laststanding[(laststanding['球隊'] == '富邦悍將')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = fubonFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '富邦悍將全年戰績':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = allstanding[(allstanding['球隊'] == '富邦悍將')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = fubonFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)
    
    elif data == '味全龍上半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = firststanding[(firststanding['球隊'] == '味全龍')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = dragonFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '味全龍下半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = laststanding[(laststanding['球隊'] == '味全龍')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = dragonFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '味全龍全年戰績':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = allstanding[(allstanding['球隊'] == '味全龍')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = dragonFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '台鋼雄鷹上半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = firststanding[(firststanding['球隊'] == '台鋼雄鷹')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = eagleFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '台鋼雄鷹下半季':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = laststanding[(laststanding['球隊'] == '台鋼雄鷹')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = eagleFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '台鋼雄鷹全年戰績':
        #TextSendMessage(text=f"收到的 data 是: {event.postback.data}"),
        selected_rows = allstanding[(allstanding['球隊'] == '台鋼雄鷹')]
        for _, row in selected_rows.iterrows():
            messages = standing_Message(row)
        reply_message = eagleFlex_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, reply_message, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)
        # messages = TextSendMessage(text=f"收到的兄弟賽程日期是: {final_date}")
        # line_bot_api.reply_message(event.reply_token, messages)

    elif data == '美國職棒大聯盟':
        country = '旅美'
        messages = cpblplayer(country=country)
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '日本職棒':
        country = '旅日'
        messages = cpblplayer(country=country)
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)
    
    elif data == '中華職棒':
        country = '中華職棒'
        messages = cpblplayer(country=country)
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '世界棒球12強地點':
        messages = twelve_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)
    
    elif data == '世界棒球經典賽地點':
        messages = wbc_Message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == 'wbc中華隊球員':
        messages = wbcnationalplayer_message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '十二強中華隊球員':
        messages = twelvenationalplayer_message()
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == 'WBC投手':
        locat = '投手'
        game = 'WBC'
        messages = nationalteamplayer(locat=locat, game=game)
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)
    
    elif data == 'WBC打者':
        locat = '打者'
        game = 'WBC'
        messages = nationalteamplayer(locat=locat, game=game)
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == 'WBC教練':
        locat = '教練'
        game = 'WBC'
        messages = nationalteamplayer(locat=locat, game=game)
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '12投手':
        locat = '投手'
        game = '十二強'
        messages = nationalteamplayer(locat=locat, game=game)
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)
    
    elif data == '12打者':
        locat = '打者'
        game = '十二強'
        messages = nationalteamplayer(locat=locat, game=game)
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)

    elif data == '12教練':
        locat = '教練'
        game = '十二強'
        messages = nationalteamplayer(locat=locat, game=game)
        quick_reply_message = TextSendMessage(text='還想了解什麼棒球賽事呢?',quick_reply=QuickReply(items))
        message=[messages, quick_reply_message]
        line_bot_api.reply_message(event.reply_token, message)








if __name__ == "__main__":
    app.run("0.0.0.0", 5000, debug=True)
    #app.run(debug=True)
