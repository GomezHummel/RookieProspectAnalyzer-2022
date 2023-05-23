import math
from flask import Flask, request, render_template
import sqlite3

app = Flask(__name__, static_folder='static')
app.debug = True

database_path = 'nba.sqlite'

@app.route("/")
def start_page():
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    ppg_min = request.args.get("ppg_min", default=0, type=float)
    ppg_max = request.args.get("ppg_max", default=1000, type=float)
    age_min = request.args.get("age_min", default=0, type=int)
    age_max = request.args.get("age_max", default=1000, type=int)
    gp_min = request.args.get("gp_min", default=0, type=int)
    gp_max = request.args.get("gp_max", default=1000, type=int)
    mpg_min = request.args.get("mpg_min", default=0.0, type=float)
    mpg_max = request.args.get("mpg_max", default=1000, type=float)
    rpg_min = request.args.get("rpg_min", default=0, type=float)
    rpg_max = request.args.get("rpg_max", default=1000, type=float)
    apg_min = request.args.get("apg_min", default=0, type=float)
    apg_max = request.args.get("apg_max", default=1000, type=float)
    spg_min = request.args.get("spg_min", default=0, type=float)
    spg_max = request.args.get("spg_max", default=1000, type=float)
    bpg_min = request.args.get("bpg_min", default=0, type=float)
    bpg_max = request.args.get("bpg_max", default=1000, type=float)
    tpg_min = request.args.get("tpg_min", default=0, type=float)
    tpg_max = request.args.get("tpg_max", default=1000, type=float)
    fta_min = request.args.get("fta_min", default=0, type=int)
    fta_max = request.args.get("fta_max", default=1000, type=int)

    query = '''
        SELECT *
        FROM complete_data
        WHERE PPG >= ? AND PPG <= ?
        AND Age >= ? AND Age <= ?
        AND GP >= ? AND GP <= ?
        AND MPG >= ? AND MPG <= ?
        AND RPG >= ? AND RPG <= ?
        AND APG >= ? AND APG <= ?
        AND SPG >= ? AND SPG <= ?
        AND BPG >= ? AND BPG <= ?
        AND TPG >= ? AND TPG <= ?
        AND FTA >= ? AND FTA <= ?
    '''
    cursor.execute(query, (ppg_min, ppg_max, age_min, age_max, gp_min, gp_max, mpg_min, mpg_max, rpg_min, rpg_max, apg_min, apg_max, spg_min, spg_max, bpg_min, bpg_max, tpg_min, tpg_max, fta_min, fta_max))

    results = cursor.fetchall()

    cursor.close()
    conn.close()

    return render_template("sets.html", results=results)


if __name__ == '__main__':
    app.run()
