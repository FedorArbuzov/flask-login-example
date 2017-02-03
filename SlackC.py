from bottle import route, run, template, post, request


@route('/')
def index():
    return 'hello'

@route('/')
def index():
    return 'hello_new'


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@post('/submit')
def index():
    text = request.get('text')
    print(text)
    return text

run(host='127.0.0.1', port=8080)