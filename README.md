# 🏦 SecureBank

Sistema Bancário com Controle de Acesso desenvolvido em Python utilizando SQLite, com foco em conceitos de **Cibersegurança** e **Estrutura de Dados**.

## 📚 Sobre o Projeto

Este projeto foi desenvolvido como atividade da disciplina de Cibersegurança e Estrutura de Dados.

O sistema implementa autenticação de usuários, controle de acesso por perfil e gerenciamento de contas bancárias utilizando banco de dados SQLite.

---

## 🚀 Tecnologias Utilizadas

- Python 3
- SQLite
- Hash SHA-256
- Git
- GitHub

---

## 📁 Estrutura do Projeto

```
SecureBank/
│
├── auth.py
├── main.py
├── logs.txt
├── README.md
│
├── database/
│   ├── connection.py
│   ├── init_db.py
│   ├── seed.py
│   ├── usuarios_repository.py
│   ├── securebank.db
│   └── __init__.py
```

---

## 🔒 Funcionalidades

### Autenticação

- Login de usuários
- Senhas protegidas com SHA-256
- Controle de acesso por perfil
- Registro de logs

### Administrador

- Cadastro de usuários
- Listagem de usuários
- Remoção de usuários *(em desenvolvimento)*
- Bloqueio de usuários *(em desenvolvimento)*

### Cliente

- Consulta de saldo *(em desenvolvimento)*
- Depósito *(em desenvolvimento)*
- Saque *(em desenvolvimento)*
- Extrato *(em desenvolvimento)*

---

## 🛡️ Segurança

O sistema utiliza algumas boas práticas de segurança:

- Senhas armazenadas utilizando hash SHA-256
- Consultas SQL parametrizadas (proteção contra SQL Injection)
- Controle de permissões por perfil (ADMIN e CLIENTE)
- Registro de logs de autenticação

---

## 🗄️ Banco de Dados

O projeto utiliza SQLite.

Tabelas:

- usuarios
- contas

---

## ▶️ Como executar

### 1 Clone o projeto

```bash
git clone https://github.com/SEU-USUARIO/SecureBank.git
```

Entre na pasta:

```bash
cd SecureBank
```

---

### 2 Crie o banco

```bash
python3 -m database.init_db
```

---

### 3 Crie o usuário administrador

```bash
python3 -m database.seed
```

---

### 4 Execute o sistema

```bash
python3 main.py
```

---

## 👤 Usuário padrão

Login

```
admin
```

Senha

```
123
```

---

## 📌 Melhorias Futuras

- MFA (Autenticação Multifator)
- Alteração de senha
- Bloqueio de usuários
- Extrato bancário
- Transferências entre contas
- Interface gráfica
- Integração com Supabase

---

## 👨‍💻 Desenvolvedores

- Fábio Antônio
- Nome do colega
