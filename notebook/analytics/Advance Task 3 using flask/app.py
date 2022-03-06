from flask import Flask, render_template, request
import pickle
import pandas as pd
# import numpy as np
# import sklearn
# import joblib
# import os
# import matplotlib
# from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    return 'hello world'# render_template('index.html')


@app.route("/index", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        # fetch the input
        Item = request.form['Item']
        Month = request.form['Month']
        Year = request.form['Year']
        # convert the input into the INT type
        Item = int(Item)
        Month = int(Month)
        Year = int(Year)
        # Create dataframe
        record = [Item]
        new_dataFile_test = pd.DataFrame(record, columns = ["Item"])
        new_dataFile_test['Month'] = Month
        new_dataFile_test['Year'] = Year
        new_x_test = new_dataFile_test
        # load the model from disk
        filename = "model/xgb_model.sav"
        xgb_model = pickle.load(open(filename, 'rb'))
        # predict the new recoed
        y_predict = xgb_model.predict((new_x_test))
        total_sale_price = format(y_predict)
        return render_template("index.html", total_sale_price=total_sale_price) #
    else:
        return render_template('index.html')



if __name__ == '__main__':
    app.run(host='localhost', port='8000', debug=True)