from flask import Flask, render_template, url_for, request, session, redirect
import hashlib
import scheduleData

app = Flask(__name__)
app.secret_key = "heheheha"

def get_hash(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

@app.route('/')
def index():
    if 'username' in session:
        return render_template("home.html", username = session["username"])
    return redirect('/login')

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect("/login")

@app.route("/register", methods = ["POST", "GET"])
def register():
    if 'username' in session:
        return redirect('/')
    if request.method == "POST":
        if scheduleData.getPassword(request.form["username"]):
            return render_template("register.html", user_taken = True)
        if request.form["password1"] != request.form["password2"]:
            return render_template("register.html", pass_diff = True)
        scheduleData.adduser(request.form["username"], get_hash(request.form["password1"]))
        return redirect("/login")
    return render_template("register.html")

@app.route("/login", methods = ["POST", "GET"])
def login():
    if 'username' in session:
        return redirect('/')
    if request.method == "POST":
        actual_password = scheduleData.getPassword(request.form["username"])
        if not actual_password:
            return render_template("login.html", no_user = True, username = request.form["username"])
        if actual_password != get_hash(request.form["password"]):
            return render_template("login.html", wrong_pass = True, username = request.form["username"])
        session["username"] = request.form["username"]
        return redirect("/")
    return render_template("login.html")

if __name__ == '__main__':
  app.run(port=5000, debug=True)
