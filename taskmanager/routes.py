from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task
# import created tables above


# user will be taken to tasks page that extends base template
@app.route("/")
def home():
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    return render_template("categories.html")


# we will be submitting form to the DB so need to include 2 methods
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method== "POST":
        # if requested method == POST, we create instance of category using imported model
        # now we need to import request from  flask at the top of the file
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        # now we need to import redirect and url_for from flask at the top of the file
        return redirect(url_for("categories"))
    return render_template("add_category.html")

# by default the normal method is GET so it'll behave as else condition and return render_template
# from outside of the block, POST block is indented, can be split to two separate functions
