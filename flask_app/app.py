import os
from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})  # Enable CORS for all origins on your API endpoints

# PostgreSQL connection
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return conn

@app.route('/')
def index():
    return "Welcome to Cricket Score Snap!"

@app.route('/api/test-batting-stats')
def get_batting_stats():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM test_batting_stats')
    stats = cursor.fetchall()
    cursor.close()
    conn.close()

    stats_list = []
    for row in stats:
        stats_list.append({
            'team': row[1],
            'player': row[2],
            'matches': row[3],
            'innings': row[4],
            'not_outs': row[5],
            'runs': row[6],
            'highest': row[7],
            'batting_average': row[8],
            'balls': row[9],
            'strike_rate': row[10],
            'hundreds': row[11],
            'fifties': row[12],
            'fours': row[13],
            'sixes': row[14],
            'catches': row[15],
            'stumping': row[16],
            'avg_runs': row[17]
        })

    return jsonify(stats_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
