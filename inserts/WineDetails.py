import pandas as pd
import sqlite3

df_winedata = pd.read_csv('C:/Users/Aluno/PycharmProjects/Bravinhos/Bravinhos_Pi/base/static/WineData.csv', sep=';')

wineDetails = df_winedata[['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
                           'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol',
                           'quality']]

conn = sqlite3.connect('db.sqlite3')

cursor = conn.cursor()

for index in wineDetails.values:
    cursor.execute(
        f'''INSERT INTO WineDetails VALUES ({index[0]}, {index[1]}, {index[2]}, {index[3]}, {index[4]}, {index[5]}, 
         {index[6]}, {index[7]}, {index[8]}, {index[9]}, {index[10]}, {index[11]})''')
