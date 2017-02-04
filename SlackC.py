from bottle import route, run, template, get, request


@route('/')
def index():
    return 'hello'

@route('/')
def index():
    return 'hello_new'


@route('/hello/<name>', method='POST')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@get('/submit')
def index():
    print(request.query_string)
    text = request.get('text')
    print(text)
    return text

run(host='127.0.0.1', port=8888)