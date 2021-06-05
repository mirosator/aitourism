from flask import Flask, render_template, request
import random
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index(interest=None):
    if request.method == "POST":
        form = request.form
        interest = form['interest']
    return render_template('index.html', interest=interest)

@app.route('/jedobrej/<name>/')
def jeBuh(name):
    cislo = random.random()
    if cislo>0.5:
        return '{} je dobrej'.format(name)
    else:
        return '{} neni dobrej'.format(name)

@app.route('/hello/')
@app.route('/hello/<name>/')
def hello(name=None):
    return render_template('hello.html', name=name)


def run(port=8000):
    app.run(debug=True, host='0.0.0.0', port=port)


if __name__ == '__main__':
    app.run(debug=True)
