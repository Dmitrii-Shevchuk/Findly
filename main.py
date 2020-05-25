from flask import Flask
from data import db_session

app = Flask(__name__)


def main():
    app.run(port=8080, host='127.0.0.1')


@app.errorhandler(401)
def error_401(error):
    return '''<h2 style="text-align:center;">Войдите, чтобы просмотреть этот раздел!</h2>'''


@app.errorhandler(404)
def error_404(error):
    return '''<h2 style="text-align:center;">Такой страницы не существует!</h2>'''


@app.errorhandler(500)
def error_500(error):
    return '''<h2 style="text-align:center;">Произошла ошибка на сервере!</h2>'''


if __name__ == '__main__':
    main()