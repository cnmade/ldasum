from base64 import encode
from flask import Flask
from flask import request


import paddlehub as hub
import json

lda_webpage = hub.Module(name="lda_webpage")


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello_world():
    if request.method == 'POST':
        data = request.form['content']
        print(data)
        results = lda_webpage.cal_doc_keywords_similarity(data)
        print(results)
        response = app.response_class(
            response=json.dumps(results, ensure_ascii=False),
            status=200,
            mimetype='application/json'
        )
        return response
    else:
        return '{"error":-1, "msg":"please input content"}' 
