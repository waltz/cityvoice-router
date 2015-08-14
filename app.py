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
<Gather timeout="15" numDigits="1" action="/select">
<Say voice="man" language="en">Press 1 for English.</Say>
<Say voice="man" language="en">Press 2 for Spanish.</Say>
<Say voice="man" language="en">Press 3 for Chinese.</Say>
</Gather>
</Response>'''

@app.route('/select', methods=['POST'])
def select():
    print '/select:', request
    print '/select:', repr(request.data)
    print '/select:', repr(request.form)
    digits = request.form.get('Digits')
    return '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
<Say voice="man" language="en">You typed the number {}</Say>
</Response>'''.format(digits)

if __name__ == '__main__':
    app.run(debug=True)