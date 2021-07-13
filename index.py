from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


if __name__ == "__main__":
    app.run()
    # парсер значений
    # сохранение результатов в бд
    # вывод из бд на клиент
    # json formatting
