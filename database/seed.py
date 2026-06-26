import hashlib
from database.connection import conectar

def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()

conn = conectar()
cursor = conn.cursor()

cursor.execute("""
INSERT INTO usuarios(login, senha_hash, tipo)
VALUES (?, ?, ?)
""", ("admin", gerar_hash("123"), "ADMIN"))

usuario_id = cursor.lastrowid

cursor.execute("""
INSERT INTO contas(usuario_id, saldo)
VALUES (?, ?)
""", (usuario_id, 1000))

conn.commit()
conn.close()

print("Administrador criado!")