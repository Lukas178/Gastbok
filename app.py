from flask import Flask, render_template, request, redirect, jsonify
import json
from datetime import datetime
import os

app = Flask(__name__)

FILE = "guestbook.json"

def load_posts():
    if os.path.exists(FILE):
        with open(FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_posts(posts):
    with open(FILE, "w", encoding="utf-8") as f:
        json.dump(posts, f, indent=2, ensure_ascii=False)

@app.route("/")
def index():
    posts = load_posts()
    posts.reverse() 
    return render_template("index.html", posts=posts)

@app.route("/add", methods=["POST"])
def add_post():
    name = request.form.get("name")
    email = request.form.get("email")
    comment = request.form.get("comment")
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    entry = {
        "name": name,
        "email": email,
        "comment": comment,
        "time": time
    }

    posts = load_posts()
    posts.append(entry)
    save_posts(posts)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)