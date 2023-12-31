from flask import Flask, render_template, url_for, request, session, redirect
import hashlib
import scheduleData
import urllib.parse

app = Flask(__name__)
app.secret_key = "heheheha"

def get_hash(string):
    return hashlib.sha256(string.encode('utf-8')).hexdigest()

def get_classes(username):
    if scheduleData.getClasses(username):
        return list(map(lambda x: x[0], scheduleData.getClasses(username)))
    return []

@app.route('/')
def index():
    if 'username' in session:
        return render_template("classlist.html", username = session["username"], classes= ["hello","goodbye","world"] + scheduleData.getClassbyname(session["username"]))
    return redirect('/classList')

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

@app.route("/classList")
def classList():
    return render_template("classList.html",classes = scheduleData.getClassbyname(session['username']) )

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if "username" not in session:
        return redirect("/login")
    if request.method == 'POST':
        if request.files["file"]:
            scheduleData.createScheduleData(session["username"], request.files["file"].read().decode("utf-8"))
            return redirect("/")
        return render_template("upload.html", error = "something went wrong")
    return render_template("upload.html")

@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template("about.html")

@app.route("/viewclass", methods=['GET', 'POST'])
def viewclass():
    return render_template("studentlist.html", clas = request.args["class"], students = scheduleData.fetchAllinClass(request.args["class"]))



if __name__ == '__main__':
  app.run(port=5000, debug=True)
