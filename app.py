# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 21:19:59 2020

@author: shvpr
"""


from flask import Flask, render_template, url_for, request
import numpy as np
import os
import pickle
import gzip

app = Flask(__name__)
f = gzip.open('./model/model.pklz', 'rb')
model = pickle.load(f)
f.close()


@app.route('/')
def home():
    return render_template('power_home.html')


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        AT = request.form['AT']
        AP = request.form['AP']
        Vacuum = request.form['Vacuum']
        RH = request.form['RH']
        data = [AT, AP, Vacuum, RH]
        vect = np.asarray(data, dtype='float32')
        vect = vect.reshape(1, -1)
        y_pred = model.predict(vect)
        efficiency = round(((y_pred[0]/495.0)*100), 2)
    return render_template('result.html', prediction=efficiency)


if __name__ == '__main__':
    # app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    # app.run(host='0.0.0.0', port=8080, use_reloader=False)
    app.run(host='0.0.0.0', port=port, debug=True)

    # if __name__ == '__main__':
    # app.run(debug=True, use_reloader=False)
    # $ export FLASK_APP=script2.py
    # $ flask run --host 0.0.0.0 --port 5001
