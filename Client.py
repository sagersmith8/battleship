from jinja2 import Template
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    tv_show = "The Office"
    return render_template("index.html", show=tv_show)


if __name__ == "__main__":
    app.run()