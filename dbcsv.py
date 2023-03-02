import csv
import sqlite3
# from flask import Flask, render_template

connection = sqlite3.connect('database.db')
curs = connection.cursor()

# Deleted and created country table
connection.execute('drop table if exists country')
print("Exist tables deleted successfully!")
connection.execute('create table country (id integer PRIMARY KEY, country_name text)')
print("Table country created successfully!")

# Deleted and created city table
connection.execute('drop table if exists city')
print("Exist tables deleted successfully!")
connection.execute('create table city (id integer REFERENCES country(id), city_name text)')
print("Table city created successfully!")

# Deleted and created animal table
connection.execute('drop table if exists animal')
print("Exist tables deleted successfully!")
connection.execute('create table animal (id integer REFERENCES country(id), animal_type text, animals text, gender text, ethnicity_name text)')
print("Table animal created successfully!")

# Deleted and created animal table
connection.execute('drop table if exists human')
print("Exist tables deleted successfully!")
connection.execute('create table human (id integer REFERENCES country(id), human text, is_required text, last_updated_date text)')
print("Table human created successfully!")

# connection.close()

with open('data.csv', newline='') as d:
    reader = csv.reader(d, delimiter=",")
    next(reader)
    for row in reader:
        print(row)

        id = int(row[0])
        country_name = row[1]
        city_name = row[2]
        gender = row[3]
        ethnicity_name = row[4]
        animal_type = row[5]
        animals = row[6]
        human = row[7]
        is_required = row[8]
        last_updated_date = row[9]

        # inserted the data to country table
        curs.execute('INSERT INTO country VALUES (?, ?)',(id, country_name))
        # inserted the data to city table
        curs.execute('INSERT INTO city VALUES (?, ?)',(id, city_name))
        # inserted the data to animal table
        curs.execute('INSERT INTO animal VALUES (?, ?, ?, ?, ?)',(id, animal_type, animals, gender, ethnicity_name))
        # inserted the data to humans table
        curs.execute('INSERT INTO human VALUES (?, ?, ?, ?)',(id, human, is_required, last_updated_date))
        connection.commit()
print("Data inputted done!")

connection.close()

# d.close()