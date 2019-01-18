from flask import Flask, render_template, request, jsonify
import pandas as pd
import pickle
import flask
# from build_model import *

app = Flask(__name__)


with open('./model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Home')

@app.route('/submit')
def submit():
    return render_template('submit.html',
                            title='Submit')

@app.route('/predict', methods=['POST','GET'])
def predict():
    if flask.request.method == 'POST':
        inputs = flask.request.form

        speech = inputs['speech_body']
        predicted = model.predict([speech])
        return render_template('predict.html',
                                title='Predict',
                                predicted=predicted[0])

if __name__ == '__main__':
    app.run(debug=True)
