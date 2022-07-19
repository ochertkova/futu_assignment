import os
from flask import *
import github
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def users():
    return render_template("users.html")

@app.route("/users/search")
def search_user():
    github_user = github.get_user(request.values.get('username'))
    return render_template("users.html", user=github_user)

@app.route("/repos")
def repos():
    return render_template("repos.html")

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False,port=port)
