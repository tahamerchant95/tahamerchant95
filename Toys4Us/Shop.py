# Will use Flask to create our website 
# python uses templating engine called jinja 

from flask import Flask 

from flask import redirect, url_for, render_template

app= Flask(__name__)

@app.route("/") # created a route to the page
def new_page():
    return render_template("index.html") # rendering template 

@app.route("/<name>") # example of dynamic URL 
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home", name="Admin")) # creating redirect function to direct user to different pages 

if __name__ == "__main__":
    app.run()




