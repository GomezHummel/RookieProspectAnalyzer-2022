import math
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_folder='static')
app.debug = True

database_path = 'nba.sqlite'

# example starting page
@app.route("/")
def start_page():
    return render_template("welcome.html")


if __name__ == '__main__':
    app.run()
