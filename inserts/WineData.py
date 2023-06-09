import pandas as pd
import sqlite3

df_winedata = pd.read_csv('C:/Users/Aluno/PycharmProjects/Bravinhos/Bravinhos_Pi/base/static/WineData.csv', sep=';')

winedata = df_winedata[['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2',
                        'variety', 'winery']]

conn = sqlite3.connect('db.sqlite3')

cursor = conn.cursor()

for index in winedata.values:
    cursor.execute(
        f'''INSERT INTO WineData VALUES ('{index[0]}', '{index[1]}', '{index[2]}', {index[3]}, {index[4]}, '{index[5]}', 
         '{index[6]}', '{index[7]}', '{index[8]}', '{index[9]}')''')
