import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    curs = connection.cursor()
    curs.execute("select * from country")
    curs.execute("select * from city")
    curs.execute("select * from animal")
    curs.execute("select * from humans")
    rows_ = curs.fetchall()
    connection.close()
    return render_template('mainpage.html', rows = rows_)