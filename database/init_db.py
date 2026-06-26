from database.connection import conectar
conn = conectar()
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    login TEXT UNIQUE NOT NULL,
    senha_hash TEXT NOT NULL,
    tipo TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS contas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    saldo REAL DEFAULT 0,
    FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)
""")

conn.commit()
conn.close()

print("Banco criado com sucesso!")