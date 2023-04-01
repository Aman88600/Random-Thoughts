from flask import Flask, render_template, request, redirect
from cs50 import SQL
app = Flask(__name__)

db = SQL("sqlite:///chats.db")

@app.route("/", methods = ["GET", "POST"])
def index():
    anime = request.form.get("anime")
    if not anime:
        db.execute("SELECT * from chats")
    else:
        db.execute("INSERT INTO chats (chat) VALUES(?)", str(anime))
    chats = db.execute("SELECT * from chats")
    db.execute("INSERT INTO test (name) VALUES(?)", str(chats))
    return render_template("index.html", chats=chats)

@app.route("/remove", methods = ["POST"])
def remove():
    db.execute("INSERT INTO test (name) VALUES(?)", "yes id")
    id = request.form.get("id")
    db.execute("INSERT INTO test (name) VALUES(?)", str(id))
    if id:
        db.execute("DELETE FROM chats WHERE id = ?", id)
        db.execute("INSERT INTO test (name) VALUES(?)", "yes id")
    else:
        db.execute("INSERT INTO test (name) VALUES(?)", "no id")

    return redirect("/")

@app.route("/clear", methods = ["GET","POST"])
def clear():
    db.execute("DELETE FROM chats")
    return redirect("/")
