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
    # list all categories
    categories = list(Category.query.order_by(Category.category_name).all())
    # cursor objec similar to array or list of objects
    return render_template("categories.html", categories=categories)


# we will be submitting form to the DB so need to include 2 methods
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        # if requested method == POST, we create instance of category
        # using imported model
        # now we need to import request from  flask at the top of the file
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        # now we need to import redirect and url_for from flask at
        # the top of the file
        return redirect(url_for("categories"))
    return render_template("add_category.html")

# by default the normal method is GET so it'll behave as else condition
# and return render_template from outside of the block, POST block is indented,
# can be split to two separate functions


@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)


@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))


@app.route("/add_task", methods=["GET", "POST"])
def add_task():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        task = Task(
            task_name=request.form.get("task_name"),
            task_description=request.form.get("task_description"),
            is_urgent=bool(True if request.form.get("is_urgent") else False),
            due_date=request.form.get("due_date"),
            category_id=request.form.get("category_id")
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add_task.html", categories=categories)
