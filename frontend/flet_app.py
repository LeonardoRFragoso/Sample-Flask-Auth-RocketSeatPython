import flet as ft

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
            if username.value == "admin" and password.value == "admin":
                status_text.value = "Login bem-sucedido!"
                status_text.color = "green"
            else:
                status_text.value = "Credenciais inválidas."
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

ft.app(target=main)
