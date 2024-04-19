# hello world를 출력하는 앱
from flask import Flask, render_template, jsonify
from flask_cors import CORS
from open_ai import request_openai

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/api/data', methods=['GET'])
def get_data():
    data = {'message': 'Hello from Flask!'}
    return jsonify(data)

@app.route('/chat', methods=['POST'])
def career_advice():
    messages = request.json['messages']
    print(message)
    result = request_openai(messages)
    print(result)
    return jsonify(result), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)