from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///todo.db'
db = SQLAlchemy(app)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, unique=False)
    is_completed = db.Column(db.Boolean)

    def __init__(self, title):
        self.title = title
        self.is_completed = False


@app.route('/')
def index():
    todos = Todo.query.all()
    return render_template("index.html", todos=todos)

app.debug = True

if __name__ == "__main__":
    app.run()