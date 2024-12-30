import time
from flask import Flask, redirect, url_for, render_template
from employees import emp_data

app = Flask(__name__)

# home page endpoint
@app.route("/")
def home():
    return render_template("home.html", title="HomePage")


# another page endpoint
@app.route("/about")
def about():
    return render_template("about.html", title="AboutPage")

# Dynamic URLS: A URL that gets generated automatically based on the inputs given by users
# path parameters
@app.route("/wish/<name>")
def wish(name):
    return f"<h1>Happy Anniversary! {name.title()}</h1>"


# path parameters (specifying integer) and giving multiple parameters
@app.route("/add/<int:num1>/<int:num2>")
def add(num1, num2):
    return f"<h1>The value of {num1} + {num2} is {num1+num2}</h1>"

#url redirection based on user input and building parameters
@app.route("/score/<name>/<int:num>")
def score(name, num):
    if num < 30:
        # redirect to fail
        time.sleep(1)
        return redirect(url_for("failed", sname=name))
    else:
        # redirect to pass
        time.sleep(1)
        return redirect(url_for("passed", sname=name))

@app.route("/pass/<sname>")
def passed(sname):
    return f"<h1>Congratulations {sname.title()}, You have passed.</h1>"


@app.route("/fail/<sname>")
def failed(sname):
    return f"<h1>Sorry  {sname.title()}, You have Failed. You need to work hard.</h1>"


# custom html Because this file is just to create different endpoints. Now we use modular programming for every page
@app.route("/evaluate/<int:num>")
def evaluate(num):
    return render_template("evaluate.html", title="evaluate", number=num)

 
## for loop in jinja template
@app.route("/employees")
def employees():
    return render_template("emploees.html", title="Employees Data", empinfo=emp_data)


@app.route("/employees/managers")
def managers():
    return render_template("managers.html", title="Managers Data", empinfo=emp_data)





if __name__ == "__main__":
    app.run(debug=True)