import csv
import sqlite3
# from flask import Flask, render_template

connection = sqlite3.connect('database.db')
curs = connection.cursor()

connection.execute('drop table if exists country')
print("Exist tables deleted successfully!")
connection.execute('create table country (id integer, country_name text, city_name text)')
print("Table country created successfully!")

# connection.close()

with open('data.csv', newline='') as d:
    reader = csv.reader(d, delimiter=",")
    next(reader)
    for row in reader:
        print(row)

        id = int(row[0])
        country_name = row[1]
        city_name = row[2]
        # gender = row[3]
        # ethnicity_name = row[4]
        # animal_type = row[5]
        # animals = row[6]
        # humans = row[7]
        # is_required = row[8]
        # last_updated_date = row[9]

        curs.execute('INSERT INTO country VALUES (?, ?, ?)', (id, country_name, city_name))
        connection.commit()
print("Data inputted done!")

connection.close()

# d.close()