from flask import Blueprint, request, redirect, url_for, render_template
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
import bcrypt

auth = Blueprint('auth', __name__)
users = {
    'prashanthgm3': bcrypt.hashpw('21!nov1996'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
    'praveenmanoharg': bcrypt.hashpw('14Oct1989'.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
}

class User(UserMixin):
    def __init__(self, id):
        self.id = id

def load_user(user_id):
    return User(user_id) if user_id in users else None

@auth.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username in users and bcrypt.checkpw(password.encode('utf-8'), users[username].encode('utf-8')):
            login_user(User(username))
            return redirect(url_for("main.dashboard"))
        return "Invalid credentials", 401
    return render_template("login.html")

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))