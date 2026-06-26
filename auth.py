import hashlib

from database.connection import conectar

ARQUIVO_LOG = "logs.txt"


def registrar_log(mensagem):

    with open(ARQUIVO_LOG, "a", encoding="utf-8") as log:

        from datetime import datetime

        data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        log.write(f"[{data}] {mensagem}\n")


def gerar_hash(senha):

    return hashlib.sha256(senha.encode()).hexdigest()


def autenticar(login, senha):

    conn = conectar()

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM usuarios
        WHERE login = ?
        """,
        (login,)
    )

    usuario = cursor.fetchone()

    conn.close()

    if usuario is None:

        registrar_log(f"Tentativa inválida ({login})")

        return None

    senha_hash = gerar_hash(senha)

    if senha_hash != usuario["senha_hash"]:

        registrar_log(f"Senha incorreta ({login})")

        return None

    registrar_log(f"Login realizado ({login})")

    return usuario