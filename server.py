from flask import Flask, render_template, request, redirect, session
from random import randint
app = Flask(__name__)


@app.route('/')
def index():
    if "secretNum" not in session:
        session["secretNum"] = randint(1, 100)
    print(session["secretNum"])
    return render_template('index.html')


@app.route('/guessing', methods=["POST"])
def guess():
    session["guess"] = request.form["guess"]
    print(session["guess"])
    return redirect('/')


@app.route('/destroy', methods=["POST"])
def destory():
    session.clear()
    return redirect('/')


if __name__ == "__main__":
    app.secret_key = "burgerboy!"
    app.run(debug=True)
