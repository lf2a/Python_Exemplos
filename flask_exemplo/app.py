import flask
from flask import request

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET', 'POST', 'PUT'])
def index():
    print(f'HEADERS: \n{request.headers}')
    print(f'\nBODY: {request.get_data()}')
    print(f'\nQUERY STRING: {dict(request.args)}')

    response = flask.Response('{"msg": "Olá Mundo!"}')
    response.headers["Content-Type"] = 'application/json'
    return response


app.run()
