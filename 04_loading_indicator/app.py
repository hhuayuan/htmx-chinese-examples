from flask import Flask, render_template, request, jsonify
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/load')
def load():
    time.sleep(5)
    return "数据加载完成！"


if __name__ == '__main__':
    app.run(debug=True)
