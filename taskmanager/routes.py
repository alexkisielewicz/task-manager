from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task
# import created tables above


# user will be taken to tasks page that extends base template
@app.route("/")
def home():
    return render_template("tasks.html")
