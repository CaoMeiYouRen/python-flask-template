# encoding=utf-8
from flask import Flask
import os

# 获取环境变量
env = os.environ
PORT = int(env.get("PORT") or 5000)
PYTHON_ENV = env.get("PYTHON_ENV") or "development"
DEBUG = PYTHON_ENV == "development"
app = Flask(__name__)
# 设置utf-8字符集
app.config["JSON_AS_ASCII"] = False


@app.route("/", methods=["GET"])
def hello_word():
    return {
        "message": "OK",
        "data": "Hello World",
    }, 200


if __name__ == "__main__":
    app.run(port=PORT, debug=DEBUG, host="0.0.0.0")
