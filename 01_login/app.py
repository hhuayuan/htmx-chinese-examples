from flask import Flask, request, render_template, make_response,url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/dashboard')
def dashboard():
    # 登录成功后的页面
    return '<h1>Welcome to DashBoard</h1><h2>Login Successful.</h2>'


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == 'admin':
        res = make_response('Login successful')
        res.headers['HX-Redirect'] = url_for('dashboard')
        return res
    else:
        # 登录失败，返回错误信息及400状态码
        return 'Login failed',400


if __name__ == '__main__':
    app.run(debug=True)
