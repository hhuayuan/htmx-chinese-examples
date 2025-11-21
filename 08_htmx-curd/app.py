from flask import Flask, render_template

fake_items = [
    {"id": 1, "name": "张三", "email": "zhangshan@gethtmx.com"},
    {"id": 2, "name": "李四", "email": "lisi@gethtmx.com"},
]


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", items=fake_items)


@app.route("/search")
def search():
    # 这里查询数据库等的逻辑
    return render_template("items.html", items=fake_items)


@app.route("/add")
def add():
    return render_template("editor.html")


@app.route("/edit/<int:id>")
def edit(id):
    data = {}
    for item in fake_items:
        if item["id"] == id:
            data = item
    return render_template("editor.html", data=data)


@app.route("/post", methods=["POST"])
def post():
    return "Successful."


@app.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    # 这里跳过后台删除的逻辑，直接返回
    return ""


if __name__ == "__main__":
    app.run(debug=True)
