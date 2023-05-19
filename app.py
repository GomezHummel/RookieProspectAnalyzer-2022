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
    query = "SELECT player_name, position, height_wo_shoes_ft_in, height_w_shoes_ft_in, weight, wingspan_ft_in, standing_reach_ft_in, body_fat_pct, hand_length, hand_width, standing_vertical_leap, max_vertical_leap, lane_agility_time, modified_lane_agility_time, three_quarter_sprint FROM draft_combine_stats"
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
