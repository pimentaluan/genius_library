# Genius Library 📚

Este projeto é um sistema de controle de empréstimos de livros desenvolvido em Django. Ele permite que administradores gerenciem o acervo de livros e os empréstimos, enquanto os leitores podem solicitar empréstimos e acompanhar seu histórico.

## 📋 Índice
- [🎯 Objetivo](#-objetivo)
- [⚙️ Funcionalidades](#-funcionalidades)
- [🛠️ Pré-requisitos](#️-pré-requisitos)
- [🚀 Instalação e Configuração](#-instalação-e-configuração)
- [🖥️ Uso do Sistema](#️-uso-do-sistema)
- [📂 Estrutura do Projeto](#-estrutura-do-projeto)
- [📝 Licença](#-licença)


## 🎯 Objetivo

O sistema foi criado para gerenciar empréstimos de livros em uma biblioteca, permitindo o controle sobre o acervo, o cadastro e a aprovação de empréstimos e devoluções, e o histórico de transações.

## ⚙️ Funcionalidades

### Para Administradores
- **Cadastro de livros:** Permite adicionar, editar ou inativar livros no acervo.
- **Registro de empréstimos:** Registrar e aprovar pedidos de empréstimo de livros.
- **Gerenciamento de devoluções:** Registrar devoluções e atualizar o status do livro.
- **Relatórios e histórico:** Visualizar e monitorar empréstimos ativos, pendentes e devolvidos.

### Para Leitores
- **Solicitação de empréstimos:** Enviar pedidos de empréstimo para aprovação.
- **Histórico de empréstimos:** Acompanhar o status e o histórico de seus empréstimos.

## 🛠️ Pré-requisitos

Certifique-se de ter instalado:
- Python 3.8+
- Django 4.0+
- PostgreSQL (ou outro banco de dados configurado no projeto)
- Git

## 🚀 Instalação e Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/pimentaluan/genius_library.git
cd genius_library
```

### 2. Crie e ative um ambiente virtual

```bash
python -m venv venv
source venv/bin/activate  # Linux ou macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o Banco de Dados

Certifique-se de que as configurações do banco de dados estão corretas no arquivo `settings.py`. O padrão é PostgreSQL, mas você pode configurar o banco de dados de sua preferência.

### 5. Execute as migrações

```bash
python manage.py migrate
```

### 6. Carregue os Dados de Exemplo (Fixtures)

Carregue dados de exemplo para usuários, livros e empréstimos.

```bash
python manage.py loaddata fixtures/users.json
python manage.py loaddata fixtures/books.json
```

### 7. Inicie o servidor

```bash
python manage.py runserver
```

Acesse o sistema em [http://localhost:8000](http://localhost:8000).

## 🖥️ Uso do Sistema

### 1. Acessar a Plataforma

Após o superusuário e outros usuários serem configurados, use as credenciais para fazer login e acessar o painel principal.

- **Email do Administrador**: `engeselt@email.com`
- **Senha do Administrador**: `Engeselt123@`

- **Emails dos Leitores**: leitor1@email.com, leitor2@email.com, etc.
- **Senha para leitores**: Engeselt123@

### 2. Administrador
- Acesse o painel de administração para gerenciar livros, empréstimos e devoluções.
- Registre novos empréstimos, aprove solicitações e atualize a quantidade de exemplares disponíveis para empréstimo.

### 3. Leitores
- Solicite o empréstimo de um livro e acompanhe o status em seu histórico.
- O pedido de empréstimo será exibido para o administrador, que poderá aprovar ou recusar.

## 📂 Estrutura do Projeto

```
genius_library
├─ .gitignore
├─ books
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ fixtures
│  ├─ books.json
│  └─ users.json
├─ loans
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ migrations
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ manage.py
├─ README.md
├─ reports
│  ├─ admin.py
│  ├─ apps.py
│  ├─ migrations
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ requirements.txt
├─ setup
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ static
│  ├─ img
│  │  ├─ login_background.webp
│  │  └─ logo.png
│  ├─ js
│  │  └─ menu.js
│  └─ styles
│     ├─ add_book.css
│     ├─ dashboard.css
│     ├─ loan_history.css
│     ├─ login.css
│     ├─ register.css
│     ├─ register_loan.css
│     ├─ reports.css
│     ├─ request_loan.css
│     ├─ return_loan.css
│     ├─ search.css
│     └─ users.css
├─ templates
│  ├─ books
│  │  ├─ add_book.html
│  │  ├─ available_books.html
│  │  ├─ edit_book.html
│  │  └─ manage_books.html
│  ├─ loans
│  │  ├─ loan_history.html
│  │  ├─ manage_loans.html
│  │  ├─ register_loan.html
│  │  ├─ request_loan.html
│  │  └─ return_loan.html
│  ├─ reports
│  │  └─ report.html
│  └─ users
│     ├─ dashboard_admin.html
│     ├─ dashboard_reader.html
│     ├─ edit_user.html
│     ├─ login_user.html
│     ├─ register_user.html
│     ├─ search_results.html
│     └─ users.html
└─ users
   ├─ admin.py
   ├─ apps.py
   ├─ backends.py
   ├─ forms.py
   ├─ migrations
   ├─ models.py
   ├─ tests.py
   ├─ urls.py
   ├─ views.py
   └─ __init__.py
```


## 📝 Licença

Este projeto foi feito por Luan Pimenta, todos os direitos reservados, 2024.
