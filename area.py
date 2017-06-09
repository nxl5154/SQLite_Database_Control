import sqlite3

conn = sqlite3.connect('factbook.db')
cursor = conn.cursor()
query_land = 'select SUM(area_land) from facts where area_land != "";'
query_water = 'select sum(area_water) from facts where area_water != "";'
total_area_land = cursor.execute(query_land).fetchall()[0][0]
total_area_water = cursor.execute(query_water).fetchall()[0][0]
land_water_ratio = total_area_land / total_area_water
print(land_water_ratio)