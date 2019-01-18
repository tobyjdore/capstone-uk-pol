from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle
import flask

app = Flask(__name__)


with open('./model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/about')
def submit():
    return render_template('about.html',
                            title='About')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if flask.request.method == 'POST':
        inputs = flask.request.form

        speech = inputs['speech_body']
        predicted = model.predict([speech])
        con_prob = str(np.round(model.predict_proba([speech])[0][0]*100,1))
        lab_prob = str(np.round(model.predict_proba([speech])[0][1]*100,1))
        return render_template('predict.html',
                                title='Predict',
                                predicted=predicted[0],
                                con_prob=con_prob,
                                lab_prob=lab_prob)

if __name__ == '__main__':
    app.run(debug=True)
