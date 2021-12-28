from application import app
from flask import render_template


@app.route("/")
@app.route("/index")
def index():
    return render_template("includes/index.html")


@app.route("/")
@app.route("/home")
def home():
    return render_template("includes/home.html")


@app.route("/")
@app.route("/about")
def about():
    return render_template("includes/about.html")


@app.route("/")
@app.route("/profile")
def profile():
    return render_template("includes/profile.html")


@app.route("/")
@app.route("/login")
def login():
    return render_template("auth/login.html")


@app.route("/")
@app.route("/regist")
def regist():
    return render_template("includes/regist.html")


@app.route("/")
@app.route("/tables")
def tables():
    return render_template("includes/tables.html")


@app.route("/")
@app.route("/convert")
def convert():
    return render_template("includes/convert.html")


@app.route("/")
@app.route("/images")
def images():
    return render_template("includes/images.html")
