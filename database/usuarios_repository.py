import hashlib
from database.connection import conectar


def gerar_hash(senha):
    return hashlib.sha256(senha.encode()).hexdigest()


def usuario_existe(login):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT id FROM usuarios WHERE login = ?",
        (login,)
    )

    usuario = cursor.fetchone()

    conn.close()

    return usuario is not None


def cadastrar_usuario(login, senha, tipo):
    if usuario_existe(login):
        return False

    conn = conectar()
    cursor = conn.cursor()

    senha_hash = gerar_hash(senha)

    cursor.execute("""
        INSERT INTO usuarios(login, senha_hash, tipo)
        VALUES (?, ?, ?)
    """, (login, senha_hash, tipo))

    usuario_id = cursor.lastrowid

    cursor.execute("""
        INSERT INTO contas(usuario_id, saldo)
        VALUES (?, ?)
    """, (usuario_id, 0))

    conn.commit()
    conn.close()

    return True


def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, login, tipo
        FROM usuarios
        ORDER BY id
    """)

    usuarios = cursor.fetchall()

    conn.close()

    return usuarios


def remover_usuario(usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM contas WHERE usuario_id = ?",
        (usuario_id,)
    )

    cursor.execute(
        "DELETE FROM usuarios WHERE id = ?",
        (usuario_id,)
    )

    conn.commit()
    conn.close()


def alterar_senha(usuario_id, nova_senha):
    conn = conectar()
    cursor = conn.cursor()

    senha_hash = gerar_hash(nova_senha)

    cursor.execute("""
        UPDATE usuarios
        SET senha_hash = ?
        WHERE id = ?
    """, (senha_hash, usuario_id))

    conn.commit()
    conn.close()


def buscar_usuario(login):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM usuarios
        WHERE login = ?
    """, (login,))

    usuario = cursor.fetchone()

    conn.close()

    return usuario