from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', a="Daniel Ivan Leyva Holguin")

@app.route("/index1")
def index1():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)