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
        return 'logged in as ' + session['username']
    return redirect('/login')

@app.route('/result', methods = ["POST", "GET"])
def result_getter():
    if not request.form.get("intvalue").isnumeric():
        return render_template('error.html')
    return render_template('mathresult.html', number = request.form.get("intvalue"), doublenumber = int(request.form.get("intvalue")) * 2)

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
