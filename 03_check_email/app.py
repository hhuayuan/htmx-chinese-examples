from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# 模拟的已注册邮箱列表
REGISTERED_EMAILS = {"test@example.com", "admin@demo.com"}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/check_email')
def check_email():
    email = request.args.get("email", "")
    exists = email in REGISTERED_EMAILS
    return render_template("email_check.html", exists=exists)

@app.route('/register', methods=["POST"])
def register():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return "<div class='message error'>所有字段都是必填项</div>", 400

    if email in REGISTERED_EMAILS:
        return "<div class='message error'>邮箱已被注册</div>", 400

    # 模拟注册成功
    REGISTERED_EMAILS.add(email)
    return "<div class='message'>注册成功！欢迎你 🎉</div>"

if __name__ == '__main__':
    app.run(debug=True)
