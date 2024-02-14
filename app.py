from flask import Flask, request, render_template, redirect, url_for
from forms import WelcomeForm, TodoForm
from models import db, Todo
from flask_migrate import Migrate


# Application setup
app = Flask(__name__)
app.config["SECRET_KEY"] = "your-secret-key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db.init_app(app)
migrate = Migrate(app, db)


# Routing
@app.route("/")
def home():
    return render_template("home.html", title="Home")


@app.route("/login", methods=["POST", "GET"])
def login():
    form = WelcomeForm()

    if form.validate_on_submit():
        name = request.form["name"]
        return render_template("welcome.html", username=name, title="Welcome")
    else:
        return render_template("login.html", title="Login", form=form)


@app.route("/todo")
def todo():
    form = TodoForm()
    todos = Todo.query.all()
    return render_template("todo_list.html", title="Todo list", form=form, todos=todos)


@app.route("/todo/add", methods=["POST"])
def add():
    new_todo = Todo(title=request.form["title"])
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("todo"))


@app.route("/todo/update/<int:todo_id>")
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.checked = not todo.checked
    db.session.commit()
    return redirect(url_for("todo"))


@app.route("/todo/delete/<int:todo_id>")
def delete(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("todo"))


# Run flask in debug mode
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
