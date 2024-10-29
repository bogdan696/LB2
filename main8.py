from flask import Flask, request

app = Flask(__name__)


@app.route("/currency", methods=["GET"])
def get_currency():

    today = request.args.get('today')


    if today:
        return "USD - 41.5"
    else:
        return "Параметр не указан", 400


if __name__ == '__main__':
    app.run(port=5000, debug=True)