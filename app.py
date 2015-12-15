# coding: utf8
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
    return u'''<?xml version="1.0" encoding="UTF-8"?>
<Response>
<Gather timeout="15" numDigits="1" action="/select">
<Say voice="alice" language="en-US">Press one for English.</Say>
<Say voice="alice" language="es-MX">Para Español oprima dos.</Say>
<Say voice="alice" language="zh-CN">按3普通话</Say>
</Gather>
</Response>'''

@app.route('/select', methods=['POST'])
def select():
    print '/select:', request
    print '/select:', repr(request.data)
    print '/select:', repr(request.form)
    digits = request.form.get('Digits')

    apps = {
        '1': 'cityvoice-garfield-pool-en',
        '2': 'cityvoice-garfield-pool-es',
        '3': 'cityvoice-garfield-pool-zh'
        }

    return '''<?xml version="1.0" encoding="UTF-8"?>
<Response>
<Redirect method="POST">https://{app}.herokuapp.com/calls</Redirect>
</Response>'''.format(app=apps[digits])

if __name__ == '__main__':
    app.run(debug=True)
