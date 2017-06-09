import sqlite3
import pandas as pd
import math

def final_pop_from_2015(row, year):
    final_pop = row['population'] * (math.e) ** (row['population_growth']/100 * (year-2015))
    return final_pop

conn = sqlite3.connect('factbook.db')
facts_db = pd.read_sql_query('select * from facts;', conn)
facts_db = facts_db.dropna()
facts_db['2050_pop'] = facts_db.apply(final_pop_from_2015, year = 2050, axis=1)
facts_db = facts_db.sort_values('2050_pop')
print(facts_db.head(10))