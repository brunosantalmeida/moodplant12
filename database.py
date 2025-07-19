import sqlite3
from datetime import datetime

def carregar_estado():
    conn = sqlite3.connect("plant_state.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS planta(
    id INTEGER PRYMARY KEY,
    humor TEXT,
    )""")

    c.execute("SELECT * FROM planta WHERE id = 1")
