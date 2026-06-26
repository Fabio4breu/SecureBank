from auth import autenticar
from database.usuarios_repository import listar_usuarios, cadastrar_usuario


def menu_admin(usuario):
    while True:
        print("\n===== MENU ADMIN =====")
        print("1 - Cadastrar usuário")
        print("2 - Listar usuários")
        print("3 - Remover usuário")
        print("4 - Bloquear usuário")
        print("0 - Sair")

        opcao = input("\nEscolha: ")

        # Logout
        if opcao == "0":
            print("\nLogout realizado.")
            break

        # Cadastro
        elif opcao == "1":

            print("\n===== CADASTRO DE USUÁRIO =====")

            login = input("Login: ")
            senha = input("Senha: ")

            print("\nTipo de usuário")
            print("1 - ADMIN")
            print("2 - CLIENTE")

            tipo_opcao = input("Escolha: ")

            if tipo_opcao == "1":
                tipo = "ADMIN"
            else:
                tipo = "CLIENTE"

            sucesso = cadastrar_usuario(login, senha, tipo)

            if sucesso:
                print("\n✅ Usuário cadastrado com sucesso!")

            else:
                print("\n❌ Esse login já existe!")

        # Listagem
        elif opcao == "2":

            usuarios = listar_usuarios()

            print("\n========== USUÁRIOS ==========")

            if not usuarios:
                print("Nenhum usuário encontrado.")
            else:
                for usuario in usuarios:
                    print(
                        f"ID: {usuario['id']} | "
                        f"Login: {usuario['login']} | "
                        f"Tipo: {usuario['tipo']}"
                    )

        # Remover
        elif opcao == "3":
            print("\nFunção Remover Usuário ainda será implementada.")

        # Bloquear
        elif opcao == "4":
            print("\nFunção Bloquear Usuário ainda será implementada.")

        else:
            print("\nOpção inválida!")


def menu_cliente(usuario):
    while True:

        print("\n===== MENU CLIENTE =====")
        print("1 - Consultar saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("0 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":
            print("\nConsultar saldo será implementado.")

        elif opcao == "2":
            print("\nDepósito será implementado.")

        elif opcao == "3":
            print("\nSaque será implementado.")

        elif opcao == "0":
            print("\nLogout realizado.")
            break

        else:
            print("\nOpção inválida!")


def main():

    print("=" * 40)
    print("         SECUREBANK")
    print("=" * 40)

    login = input("Login: ")
    senha = input("Senha: ")

    usuario = autenticar(login, senha)

    if usuario is None:
        print("\nUsuário ou senha inválidos.")
        return

    print(f"\nBem-vindo(a), {usuario['login']}!")

    if usuario["tipo"] == "ADMIN":
        menu_admin(usuario)

    elif usuario["tipo"] == "CLIENTE":
        menu_cliente(usuario)

    else:
        print("\nUsuário sem permissão.")


if __name__ == "__main__":
    main()