# run this class for running server for data exchange between user-input and chatbot

from flask import Flask, request

from actions import handle_user_input

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello world'


@app.route('/send-user-input', methods=['POST'])
def receive_user_input():
    handle_user_input(request)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
