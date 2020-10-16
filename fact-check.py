from flask import Flask, request, render_template, redirect, flash, session
import jinja2

app = Flask(__name__)
app.secret_key = "fdjhsut9grepui32ao489tp(W#RE&#fkjah"
app.jinja_env.undefined = jinja2.StrictUndefined
app.config['PRESERVE_CONTEXT_ON_EXCEPTION'] = True

@app.route("/")
def home():
    """Display home page, where a user can enter the URL to a news article."""

    return render_template("home.html")

# @app.route("/fact-check")
# def fact_check():

#     return render_template("fact-check.html", article_address=article_address)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0")