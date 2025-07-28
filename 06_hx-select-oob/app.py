from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/oob')
def oob():
    return render_template("oob.html")

@app.route('/select')
def select():
    return render_template("select.html")

if __name__ == '__main__':
    app.run(debug=True)
