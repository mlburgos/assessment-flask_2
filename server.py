from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# YOUR ROUTES GO HERE
@app.route('/')
def homepage():
    return render_template("index.html")


@app.route('/application-form')
def application():
    jobs = ['Software Engineer', 'QA Engineer', 'Product Manager']
    return render_template("application-form2.html",
                           jobs=jobs,
                           )


@app.route('/application-success', methods=["POST"])
def app_success():
    name = request.form.get('firstname') + " " + request.form.get('lastname')
    title = request.form.get('title')
    salary_req = float(request.form.get('salaryRequirement'))

    if salary_req == round(salary_req, 0):
        formatted_salary_req = "{:20,.0f}".format(salary_req)
    else:
        formatted_salary_req = "{:20,.2f}".format(salary_req)

    return render_template("application-response.html",
                                   name=name,
                                   title=title,
                                   salary_req=formatted_salary_req,
                                   )


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
