import os
from flask import *
import github
import stats
import utils
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/users")
def users():
    return render_template("users.html")

@app.route("/users/<username>")
def get_user(username):
    github_user = github.get_user(username)
    fav_languages = stats.fav_languages(github_user)
    return render_template("users.html", user=github_user,lang=fav_languages)
    
@app.route("/users/search")
def search_user():
    return get_user(request.values.get('username'))

@app.route("/repos")
def repos():
    return render_template("repos.html")

@app.route("/repos/<owner>/<reponame>")
def show_repo(owner,reponame):
    github_repo = github.get_repo(owner,reponame)
    if github_repo:
        cr_d = utils.format_date(github_repo['created_at'])
        up_d = utils.format_date(github_repo['updated_at'])
        p_d = utils.format_date(github_repo['pushed_at'])
        dates = {'created_at': cr_d, 'updated_at':up_d, 'pushed_at':p_d}

    return render_template("repos.html", owner=owner, repo=github_repo, dates=dates)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__": 
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False,port=port)
