from flask import Flask, render_template, request
import random
import _pickle as cPickle
import numpy
app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        form = request.form
        interest = form['interest']
        type = form['type']
        nationality = form['nationality']

        predict = []
        predict.append(int(nationality))
        predict.append(int(type))
        predict.append(int(interest))

        dst_lst = ['tenis','minigolf','volejbal','zámek','hrad','kostel','vodopád','kopec','skála']
        with open('novy_classifier.pkl', 'rb') as fid:
            model = cPickle.load(fid)
        #old---
        # x = model.predict([predict])
        # vysledek = dst_lst[x.item(0)]
        #old---
        x = model.predict_proba([predict])
        print("pravdepodobnosti:", x.tolist())
        l = numpy.argsort(-x)[:3] #seradi indexy od nejvetsiho - nejvetsi pravdepodobnosti
        print("serazeno:", l)
        print("nejvyssi:", l.item(0))
        #print(l)
        vysledek = dst_lst[l.item(0)]
        id = [l.item(0),l.item(1),l.item(2)]
        return render_template('vysl.html', vysledek=id)
    else:
        return render_template('index.html')

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

@app.route('/watafak')
def watafak():
    dst_lst = ['tenis', 'minigolf', 'volejbal', 'zámek', 'hrad', 'kostel', 'vodopád', 'kopec', 'skála']
    with open('novy_classifier.pkl', 'rb') as fid:
        model = cPickle.load(fid)
    x = model.predict([[1,1,1]])
    print(dst_lst[x.item(0)])
    return dst_lst[x.item(0)]

def run(port=8000):
    app.run(debug=True, host='0.0.0.0', port=port)


if __name__ == '__main__':
    app.run(debug=True)