import pandas as pd
import numpy as np
import pickle
import gzip
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

xls = pd.ExcelFile(r"C:\Users\shvpr\Downloads\data\Folds5x2_pp.xlsx")
print(xls.sheet_names)

df = pd.read_excel(r"C:\Users\shvpr\Downloads\data\Folds5x2_pp.xlsx",
                   sheet_name='Sheet1')

X = df.drop('PE', axis=1)
y = df['PE']
pipeline = Pipeline(steps=[
    ('std_scaler', StandardScaler()),
])
df_prepared = pipeline.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(
    df_prepared, y, test_size=0.2, random_state=42)
print(len(X_train), ' samples in training data\n',
      len(X_test), ' samples in test data\n', )
param_grid = [

    {'bootstrap': [False], 'n_estimators':[10, 30],
     'max_features':[1, 2, 3, 4]}]
forest_reg = RandomForestRegressor()
grid_search = GridSearchCV(forest_reg, param_grid=param_grid, cv=5,
                           scoring='neg_mean_squared_error')
grid_search.fit(X_train, y_train)

# Saving the model to disk
# store the object

f = gzip.open(r'C:\Users\shvpr\Downloads\model\model.pklz', 'wb')
pickle.dump(grid_search, f)
f.close()

# restore the object
f = gzip.open(r'C:\Users\shvpr\Downloads\model\model.pklz', 'rb')
model = pickle.load(f)
f.close()

# NB_spam_model = open('NB_spam_model.pkl','rb')

print(model.predict([[9.94, 40.6, 1018.9, 68.51]]))
