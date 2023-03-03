import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('mainpage.html')

@app.route('/table1')
def table1():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    curs = connection.cursor()
    curs.execute("select * from country, animal where (animal.id = country.id and country.country_name = 'China')")
    rows_ = curs.fetchall()
    connection.close()
    return render_template('table1.html', rows = rows_)

@app.route('/table2')
def table2():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    curs = connection.cursor()
    curs.execute("select * from country, animal where (animal.id = country.id and country.country_name = 'United States')")
    rows_ = curs.fetchall()
    connection.close()
    return render_template('table2.html', rows = rows_)

@app.route('/table3')
def table3():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    curs = connection.cursor()
    curs.execute("select * from country, animal where (animal.id = country.id and country.country_name = 'Brazil')")
    rows_ = curs.fetchall()
    connection.close()
    return render_template('table3.html', rows = rows_)

@app.route('/table4')
def table4():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    curs = connection.cursor()
    curs.execute("select * from country, animal where (animal.id = country.id and country.country_name = 'Canada')")
    rows_ = curs.fetchall()
    connection.close()
    return render_template('table4.html', rows = rows_)

if __name__ == '__main__':
    app.run(debug=True)

# curs.execute("select * from city")
# curs.execute("select * from animal")