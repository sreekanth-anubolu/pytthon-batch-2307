

from flask import Flask, render_template, request, redirect
import bcrypt

from db_conn import PG_CONN

app = Flask(__name__)

salt = bcrypt.gensalt()

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


if __name__ == "__main__":
    app.run(debug=True)