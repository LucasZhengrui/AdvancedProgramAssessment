import sqlite3
from flask import Flask, render_template

application = Flask(__name__)

@application.route('/')
def indexdb():
    connection = sqlite3.connect('basice_database.db')
    connection.row_content = sqlite3.Row
    tag = connection.cursor()
    tag.execute("select * from table_example")
    rows = tag.fetchall()
    connection.close()
    return render_template('mainpage.html', rows = rows)