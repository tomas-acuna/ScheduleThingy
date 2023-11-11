from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('signup.html')

@app.route('/result', methods = ["POST", "GET"])
def result_getter():
  if not request.form.get("intvalue").isnumeric():
    return render_template('error.html')
  return render_template('mathresult.html', number = request.form.get("intvalue"), doublenumber = int(request.form.get("intvalue")) * 2)

if __name__ == '__main__':
  app.run(port=5000, debug=True)
