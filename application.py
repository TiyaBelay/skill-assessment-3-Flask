from flask import Flask, render_template, request
import jinja2

app = Flask(__name__)

app.secret_key = 'this-should-be-something-unguessable'

app.jinja_env.undefined = jinja2.StrictUndefined

@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

@app.route("/application-form")
def app_form():
    """Show an application form page."""

    return render_template("application-form.html")

@app.route("/application", methods=["POST"])
def submit_app_form():
    """Show the application response page."""

    firstname = request.form.get("fstname")
    lastname = request.form.get("lstname")
    salary = request.form.get("salaryreq")
    position = request.form.get("job")

    return render_template("application-response.html",
                            fstname=firstname,
                            lstname=lastname,
                            salaryreq=salary,
                            job=position,
                            )


if __name__ == "__main__":
    app.run(debug=True)
