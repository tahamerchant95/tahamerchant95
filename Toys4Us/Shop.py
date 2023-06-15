# Will use Flask to create our website 

from flask import Flask 

from flask import redirect, url_for

app= Flask(__name__)

@app.route("/") # created a route to the page
def new_page():
    return "This is the new page <h1>hello World</h1>"

@app.route("/<name>") # example of dynamic URL 
def user(name):
    return f"Hello {name}"

@app.route("/admin")
def admin():
    return redirect(url_for("home")) # creating redirect function to direct user to different pages 

if __name__ == "__main__":
    app.run()




