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
        SELECT p."NAME", CAST(p."AGE" AS INT) AS "AGE", dcs.position, p."GP", p."MPG", p."PPG", p."RPG", p."APG",
        p."SPG", p."BPG", p."TPG", p."FTA",
        p."FT%", p."2PA", p."2P%", p."3PA", p."3P%", p."eFG%", p."TS%", p."ORtg", p."DRtg",
        SUBSTR(dcs.height_wo_shoes_ft_in, 1, INSTR(dcs.height_wo_shoes_ft_in, '.')-1) || '"' AS height_wo_shoes_ft_in,
        dcs.weight,
        SUBSTR(dcs.wingspan_ft_in, 1, INSTR(dcs.wingspan_ft_in, '.')-1) || '"' AS wingspan_ft_in,
        SUBSTR(dcs.standing_reach_ft_in, 1, INSTR(dcs.standing_reach_ft_in, '.')-1) || '"' AS standing_reach_ft_in,
        dcs.hand_length, dcs.hand_width, dcs.max_vertical_leap
        FROM players p
        JOIN draft_combine_stats dcs ON p."NAME" LIKE '%' || dcs.player_name || '%';
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
