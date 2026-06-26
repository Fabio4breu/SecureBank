import sqlite3
import os

DB_NAME = os.path.join(os.path.dirname(__file__), "securebank.db")

def conectar():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn