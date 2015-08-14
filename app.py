from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/call', methods=['POST'])
def call():
    print '/call:', request
    print '/call:', repr(request.data)
    print '/call:', repr(request.form)
    return '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
<Gather timeout="10" numDigits="1" action="/select">
<Say voice="man" language="en">Speak friend and enter</Say>
</Gather>
</Response>'''

@app.route('/select', methods=['POST'])
def select():
    print '/select:', request
    print '/select:', repr(request.data)
    print '/select:', repr(request.form)
    return '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
<Say voice="man" language="en">Speak friend and enter</Say>
</Response>'''

if __name__ == '__main__':
    app.run(debug=True)