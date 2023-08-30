
from flask import Flask

from flask import render_template

app = Flask(__name__)

print(app)

@app.route('/')
def hello_world():
    print("I am from hello_world method")
    return "Hello, Flask World!"


@app.route("/home")
def home():
    print("home method called")
    return """
    <html>
        <h1 style='color:green;'> This is a home page by Flask Application h1 tag </h1>
        <h2 style='color:blue;'> This is a home page by Flask Application h2 tag </h2>
        <h3 style='color:red;'> This is a home page by Flask Application h3 tag </h3>
    </html>"""


# Path variable
@app.route("/user/<username>")
def path_variable_example(username):
    return f"<h1> Hi  <p style='color:orange'> {username} </p> <h1>"


# Path variable
@app.route("/add/<x>/<y>")
def add(x, y):
    if x.isdigit() and y.isdigit():
        return f"<h1> Add Function  <p style='color:orange'> {x} + {y} =  {int(x) + int(y)} </p> <h1>"
    else:
        return "<p style='color:red'> Error - Invalid Data  </p>"


@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/hello/<name>")
def hello(name):
    return render_template("hello.html", username=name)


@app.route("/students/list")
def get_students_list():
    students = ["momin", "rubina", "archana", "harikrupa", "harish"]
    return render_template("students_list.html", data=students, add_button=False)


from flask import request

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        print(request.form)
        username = request.form["username"]
        return f"Logged in as {username}"


if __name__ == "__main__":
    app.run(debug=True)
