from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/post',methods=['POST'])
def oob():
    print(request.values)
    return "Submitted!"


if __name__ == '__main__':
    app.run(debug=True)
