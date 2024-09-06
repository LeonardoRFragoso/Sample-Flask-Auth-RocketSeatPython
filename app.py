import threading
from backend.flask_app import create_flask_app
import flet as ft
from frontend.flet_ui import main

# Iniciar o servidor Flask em uma thread separada
def start_flask():
    app = create_flask_app()
    app.run(debug=True, use_reloader=False)

# Iniciar o Flask em uma thread separada
flask_thread = threading.Thread(target=start_flask, daemon=True)
flask_thread.start()

# Executar o front-end com Flet
ft.app(target=main)
