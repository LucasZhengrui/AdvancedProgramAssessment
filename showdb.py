import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    curs = connection.cursor()
    curs.execute("select * from country, city, animal where (city.id = animal.id and animal.id = country.id and city.id = country.id and country.id <= 200 and country.country_name = 'China' and animal.gender='Male')")
    rows_ = curs.fetchall()
    connection.close()
    return render_template('mainpage.html', rows = rows_)

if __name__ == '__main__':
    app.run(debug=True)

# curs.execute("select * from city")
# curs.execute("select * from animal")
# curs.execute("select * from humans")