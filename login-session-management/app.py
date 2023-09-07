import bcrypt

from flask import Flask, request, render_template, redirect

from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from db_conn import PG_CONN

app = Flask("Auth")

app.config["SECRET_KEY"] = "SECRET_KEY_TO_GEN_SESSION"

login_manager = LoginManager(app)

salt = "$2b$12$KHi2VI7H2YhWeMSeF45zbO".encode("utf-8")

class User(UserMixin):

    def __init__(self, id, email, password):
        self.email = email
        self.password = password
        self.id = id

    @staticmethod
    def get(email):
        query = "SELECT * FROM USERPROFILE WHERE EMAIL=%s"
        conn = PG_CONN.get_db_connection()
        curr = conn.cursor()
        curr.execute(query, (email,))
        rs = curr.fetchone()
        if rs:
            return User(rs[0], rs[2], rs[3])
        else:
            return None
@login_manager.user_loader
def load_user(user_email):
    return User.get(user_email)
@app.route("/register")
def render_register_page():
    return render_template("registration.html")

@app.route("/register/user", methods=["POST"])
def create_user():
    name = request.form["name"]
    email = request.form["email"]
    password = request.form["password"].encode("utf-8")
    passwrod_hash = bcrypt.hashpw(password, salt).decode("utf-8")
    print(passwrod_hash)
    print(name, email, password)
    conn = PG_CONN.get_db_connection()
    curr = conn.cursor()
    QUERY = "INSERT INTO USERPROFILE(name, email, password) values(%s, %s, %s);"
    curr.execute(QUERY, (name, email, passwrod_hash))
    conn.commit()
    curr.close()
    conn.close()
    return redirect("/register")


def is_valid_password(stored_password, input_password):
    input_password = input_password.encode("utf-8")
    hash = bcrypt.hashpw(input_password, salt).decode("utf-8")
    print(stored_password)
    print(hash)
    if hash == stored_password:
        return True
    else:
        return False

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        email = request.form["email"]
        password = request.form["password"]
        user = User.get(email)
        if user:
            stored_password = user.password
            if is_valid_password(stored_password, password):
                login_user(user)
                return redirect("/home")
            else:
                return render_template("login.html", invalid_user=True)
        else:
            return render_template("login.html", invalid_user=True)



@app.route("/home")
@login_required()
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)