from flask import request
import pickle
import math
import locale
from flask import Flask, render_template, jsonify
# from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = 'c8faaf33aaa751c1270e70af5c21fa75'

@app.route('/', methods=['GET'])
def index():
    return render_template("data.html")


model = pickle.load(open('item_sales.pkl','rb'))

@app.route('/result', methods=['POST'])
def predict():
    store = float(request.form['store'])
    items = float(request.form['items'])
    day = float(request.form['day'])
    month = float(request.form['month'])
    year = float(request.form['year'])

    output = math.floor(model.predict([[store, items, day, month, year]]))

    locale.setlocale(locale.LC_ALL, '')
    output = locale.format("%d", output, grouping=True)
    return "Predicted Sales for " + str(store) + " store " + str(items) + " items on " \
    + str(day) + ":" + str(month) + ":" + str(year) + " is :- " + str(output)




if __name__ == '__main__':
    app.run(debug=True)
