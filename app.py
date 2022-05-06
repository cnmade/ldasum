from flask import Flask
from flask import request


import paddlehub as hub
import json

lda_news = hub.Module(name="lda_news")

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        data = request.form['content']
        print(data)
        results = lda_news.cal_doc_keywords_similarity(data)
        print(results)
        return json.dumps(results) 
    else:
        return '{"error":-1, "msg":"please input content"}' 