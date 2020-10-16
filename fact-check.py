from flask import Flask, request, render_template, redirect, flash

app = Flask(__name__)
app.secret_key = "fdjhsut9grepui32ao489tp(W#RE&#fkjah"

@app.route("/")
def home():
    """Display home page, where a user can enter the URL to a news article."""

    return render_template("home.html")