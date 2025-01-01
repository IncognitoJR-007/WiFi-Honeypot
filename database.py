import sqlite3

DB_PATH = 'honeypot.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS packets (
        id INTEGER PRIMARY KEY,
        src_ip TEXT,
        dst_ip TEXT,
        protocol TEXT,
        length INTEGER,
        latitude REAL,
        longitude REAL,
        city TEXT,
        country TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    conn.commit()
    conn.close()

def log_packet(src_ip, dst_ip, protocol, length, latitude, longitude, city, country):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO packets (src_ip, dst_ip, protocol, length, latitude, longitude, city, country)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (src_ip, dst_ip, protocol, length, latitude, longitude, city, country))
    conn.commit()
    conn.close()

def fetch_logs():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM packets ORDER BY timestamp DESC')
    logs = cursor.fetchall()
    conn.close()
    return logs

init_db()
