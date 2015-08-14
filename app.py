from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/call', methods=['POST'])
def call():
    print request
    print repr(request.data)
    print repr(request.form)
    return 'Goodbye World'

if __name__ == '__main__':
    app.run(debug=True)