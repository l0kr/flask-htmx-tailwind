import data
from flask import Flask, request
from flask.templating import render_template
from flask_assets import Bundle, Environment




app = Flask(__name__)


assets = Environment(app)
css = Bundle("src/main.css", output="dist/main.css")
assets.register("css", css)
css.build()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search_todo():
    search_term = request.form.get("search")

    if search_term == None :
        return render_template("todo.html", todos=[])

    res_todos = []
    for todo in data.todos:
        if search_term in todo["title"]:
            res_todos.append(todo)

    return render_template("todo.html", todos=res_todos)

if __name__ == "__main__":
    app.run(debug=True)

