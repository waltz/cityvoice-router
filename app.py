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
    return '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
    <Say voice="man" language="en">Speak friend and enter</Say>
</Response>'''

if __name__ == '__main__':
    app.run(debug=True)