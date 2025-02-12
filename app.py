from flask import Flask,redirect,url_for,render_template,request,session,flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "apak143"
app.permanent_session_lifetime = timedelta(minutes=5)

# In session : it stores data temporarily on the the website 

@app.route("/")
def home():
    return render_template("index.html")

# Sessions
@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        session.permanent = True # It considers that the data will stay on the website tile the lifetime 
        user = request.form["username"]
        session["user"] = user
        flash("Login Successful!","success")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("Already Logged in!","success")
            return redirect(url_for("user"))
        return render_template("login.html")


@app.route("/forgot_password",methods=["GET","POST"])
def forgot_password():
    return render_template("forgot_password.html")




@app.route("/user",methods=["GET","POST"])
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user = user)
    else:
        flash("You are not logged in!","success")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    if "user" in session:
        flash("You have been logged out successfully!","success")
        session.pop("user",None)
        return redirect(url_for("login"))
    else:
        flash("You have already logged out!")
        return redirect(url_for("login")) 



if __name__ == "__main__":
    app.run(debug=True)
