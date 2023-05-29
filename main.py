from dotenv import load_dotenv
from flask import Flask, request, abort
from hyperdb import HyperDB
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import numpy as np
import pandas as pd

from src.models import OpenAIModel
from src.database import CustomizeHyperDB
from src.utils import data_preprocessing

import os
load_dotenv()

app = Flask(__name__)

line_bot_api = LineBotApi(os.getenv('LINE_CHANNEL_ACCESS_TOKEN'))
handler = WebhookHandler(os.getenv('LINE_CHANNEL_SECRET'))
model = OpenAIModel(os.getenv('OPENAI_API_KEY'))
db = CustomizeHyperDB()

TOKENS_LIMIT = 1800
DOCUMENTS_NAME = 'taoyuan-airport-faq.csv'
DB_FILE_NAME = 'hyperdb.pickle.gz'

@app.route('/callback', methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret.')
        abort(400)
    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    try:
        query = event.message.text.strip()
        query_vector = np.array(model.embedding(query))
        documents = db.query(query_vector, top_k=5)
        messages = [{
            'role': 'system',
            'content': '你現在是個資深客服人員，能夠透過使用者的問題，回去文本中尋找答案'
        }, {
            'role': 'user',
            'content': f"""
            把問題誠實地回答，使用下面提供的文本
            
            {str(documents)[:TOKENS_LIMIT]}
            
            如果答案不在以下文本中，請說“我不知道”。 
            
            Q: {query}
            A:
            """
        }]

        _, content = model.chat_completion(messages)
    except Exception as e:
        print(str(e))
        content = '請重新輸入'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=content))


@app.route('/', methods=['GET'])
def home():
    return 'Hello World!'


if __name__ == '__main__':
    if DB_FILE_NAME in os.listdir('./'):
        print('loading data')
        db.load(DB_FILE_NAME)
    else:
        if DOCUMENTS_NAME not in os.listdir('./'):
            raise FileNotFoundError(f'{DOCUMENTS_NAME} not found')
        print('data preprocessing...')
        documents, vectors = data_preprocessing(DOCUMENTS_NAME, model)
        print('data preprocessed')
        db.add_documents(documents, vectors)
        print('saving data')
        db.save(DB_FILE_NAME)
    app.run(host='0.0.0.0', port=8000)
