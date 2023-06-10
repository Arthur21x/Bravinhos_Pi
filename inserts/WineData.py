import pandas as pd
import sqlite3

df_winedata = pd.read_csv('C:/Users/ACER/PycharmProjects/Bravinhos/Bravinhos_Pi/base/static/WineData.csv', sep=';')

winedata = df_winedata[['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2',
                        'variety', 'winery']]

conn = sqlite3.connect('C:/Users/ACER/PycharmProjects/Bravinhos/Bravinhos_Pi/db.sqlite3')

cursor = conn.cursor()

for value, index in enumerate(winedata.values):
    cursor.execute(
        f'''INSERT INTO Wine_general_winedata VALUES ({value+1}, "{index[0]}", "{index[1]}", "{index[2]}", {index[3]}, "{index[9]}", "{index[5]}",
         "{index[6]}", "{index[7]}", "{index[8]}", {index[4]})''')
    conn.commit()

cursor.close()
conn.close()
