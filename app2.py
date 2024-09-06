import os
import flet as ft
from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from models.user import User
from database import db
import bcrypt
from sqlalchemy.exc import SQLAlchemyError
import threading
import requests

# Configuração do Flask (Back-end)
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "your_default_secret_key")
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'mysql+pymysql://root:admin123@127.0.0.1:3306/flask-crud')

login_manager = LoginManager()
db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Por favor, preencha todos os campos."}), 400

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.checkpw(str.encode(password), str.encode(user.password)):
        login_user(user)
        return jsonify({"message": "Autenticação realizada com sucesso!"})

    return jsonify({"message": "Credenciais inválidas"}), 400

# Iniciar o servidor Flask em uma thread separada
def start_flask():
    app.run(debug=True, use_reloader=False)

# Função de Frontend (Flet)
def main(page: ft.Page):

    # Definir o tema escuro e fundo escuro
    page.theme_mode = "dark"
    page.bgcolor = "#1a1a1a"  # Fundo escuro
    page.padding = 0
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Função para lidar com login
    def login_clicked(e):
        if username.value == "" or password.value == "":
            status_text.value = "Por favor, preencha todos os campos."
        else:
            # Fazendo a requisição ao back-end (Flask)
            response = requests.post(
                "http://127.0.0.1:5000/login",
                json={"username": username.value, "password": password.value}
            )
            # Verificando a resposta da API
            if response.status_code == 200:
                status_text.value = "Login bem-sucedido!"
                status_text.color = "green"
            else:
                status_text.value = response.json().get("message", "Erro no login")
                status_text.color = "red"
        page.update()

    # Definir campos de texto minimalistas com estilo escuro
    username = ft.TextField(
        label="Usuário", 
        width=320, 
        height=50,
        border_radius=6, 
        bgcolor="#333333",  # Fundo do campo mais escuro
        border_color="#555555",  # Borda mais clara
        text_size=16,
        text_style=ft.TextStyle(color="white"),  # Texto branco
        content_padding=ft.Padding(10, 10, 10, 10)
    )
    password = ft.TextField(
        label="Senha", 
        password=True, 
        width=320, 
        height=50,
        border_radius=6, 
        bgcolor="#333333", 
        border_color="#555555",
        text_size=16,
        text_style=ft.TextStyle(color="white"),
        content_padding=ft.Padding(10, 10, 10, 10)
    )

    # Botão de login com cor escura e contraste
    login_button = ft.Container(
        content=ft.ElevatedButton(
            "Entrar", 
            on_click=login_clicked,
            bgcolor="#4CAF50",  # Botão verde para contraste
            color="white",
            width=320,
            height=50
        ),
        border_radius=8,
        ink=True,
        padding=ft.Padding(0, 10, 0, 10)
    )

    # Mensagem de status para exibir feedback de erros ou sucesso
    status_text = ft.Text("", size=14, color="red")

    # Organizar os elementos em uma coluna centralizada com espaçamento
    login_form = ft.Column(
        [
            ft.Text("Login", size=32, weight="bold", color="white"),  # Texto branco para contraste
            username,
            password,
            login_button,
            status_text
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    # Adicionar o formulário centralizado na página com sombra suave
    page.add(
        ft.Container(
            content=login_form,
            alignment=ft.alignment.center,
            padding=40,
            width=420,
            height=520,
            border_radius=12,
            bgcolor="#262626",  # Fundo do container escuro
            shadow=ft.BoxShadow(
                blur_radius=30,
                spread_radius=1,
                color="#000000"
            )
        )
    )

# Iniciar o Flask em uma thread separada
flask_thread = threading.Thread(target=start_flask, daemon=True)
flask_thread.start()

# Executar o front-end com Flet
ft.app(target=main)
