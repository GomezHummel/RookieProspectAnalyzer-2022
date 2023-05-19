import math
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_folder='static')
app.debug = True

database_path = 'nba.sqlite'

# example starting page
@app.route("/")
def start_page():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    # Execute the query
    query = '''
        SELECT *
        FROM complete_data
    '''
    cursor.execute(query)

    # Fetch all the results
    results = cursor.fetchall()

    # Close the database connection
    cursor.close()
    conn.close()

    # Pass the results to the template for rendering
    return render_template("sets.html", results=results)



if __name__ == '__main__':
    app.run()
