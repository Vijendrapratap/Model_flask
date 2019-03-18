import pandas as pd
import math
import numpy as np
from pandas.api.types import is_numeric_dtype
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score, mean_squared_error, accuracy_score
import warnings
warnings.filterwarnings("ignore")
import pickle
from sklearn.linear_model import LinearRegression

data = pd.read_csv("train.csv")
y = data['sales']
data = data.drop(columns ='sales')

data['date'] = pd.to_datetime(data['date'], errors='coerce')
data['year'],data['month'],data['day'] = data.date.dt.year, data.date.dt.month, data.date.dt.day

data = data.drop(columns = 'date')

from sklearn.ensemble import RandomForestRegressor
regressorand = RandomForestRegressor()
rand = regressorand.fit(data, y)

# from sklearn.model_selection import GridSearchCV
# grid_param = {penalty :[‘l2’, ‘l1’, ‘elasticnet’]
#              loss : ["squared_epsilon_insensitive",‘squared_loss’]}
#
# gd_sr = GridSearchCV(estimator = regressor, param_grid = grid_param, scoring = 'accuracy', cv = 5, n_jobs = -1)
# grid = gd_sr.fit(x_train, y)

pickle.dump(regressorand, open('item_sales.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('item_sales.pkl','rb'))


# day = int(input("Enter date  "))
# month = int(input("Enter month  "))
# year = int(input("Enter year  "))
# store_number = int(input("Enter store_number (1-50) "))
# item_number = int(input("Enter item_number(1-)  "))
#
# print(abs(math.floor(model.predict([[store_number, item_number, year, month, day]]))))
