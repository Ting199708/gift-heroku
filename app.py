from flask import Flask, request, abort
from urllib.request import urlopen
#from oauth2client.service_account import ServiceAccountCredentials

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError,LineBotApiError
)

################################

from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('4VfcF4pQ7zfweO+ExrrKHJSeUtmE9trHLwc2yHeuTwoQLJfHiWl57wogOi5KWxWqwzHCRffM6rSMSwfpWc6k6x5E1SzCRXbKDEKkHaYX0/bCEgDMiVlYMscyCUCLq/N40iGknnnzBYNzor1+Q8qGKQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('04c0ccc463c35b364c721fd1426da0f5')
#Name list
name_list = ['丁之正','蕭博鈞','張裕宏','張之叡','黃煜庭','鄒承翰','許子亮','賴翰樟','鄭聖耀','林亦壎']
passwd_list = ['yJ1238tde24']
# 監聽所有來自 /callback 的 Post Request
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
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print(event)
    text=event.message.text

    if (text=="交換禮物"):
        reply_text = "請先告訴我你的名字"
        #Your user ID

    for i in name_list:
        if(text==i):
            reply_text = i+"你好，再來請告訴我你的密碼"
            break
    for passwd in range(passwd_list.size()):
        if(text == passwd_list[passwd]):
            reply_text = "驗證成功！\n請你依照以下資訊進行配送"

    message = TextSendMessage(reply_text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
