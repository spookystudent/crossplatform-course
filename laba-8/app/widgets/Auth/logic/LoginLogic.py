from PyQt5.QtWidgets import QMessageBox


import requests


class LoginLogic:
    def __init__(self, auth_app):
        from core.app import AuthApp
        self.auth_app: 'AuthApp' = auth_app
        self.base_api_url = self.auth_app.BASE_API_URL

    def handle_login(self):
        name = self.auth_app.login_form.name_input.text()
        password = self.auth_app.login_form.password_input.text()

        if not name or not password:
            self.show_error("Заполните все поля")
            return

        try:
            response = requests.post(
                f"{self.base_api_url}/auth/login",
                json={"name": name, "password": password},
            )

            if response.status_code == 200:
                self.on_login_success(response.json(), name)
            else:
                self.on_login_failure(response)

        except requests.exceptions.RequestException:
            self.on_connection_error()

    def on_login_success(self, response_data: dict, username):
        self.auth_app.main_window.set_user_info(username)
        self.auth_app.show_main_window()

    def on_login_failure(self, response: 'requests.Response'):
        error_message = response.json().get("message", "Неверные учетные данные")
        self.show_error(error_message)

    def on_connection_error(self):
        self.show_error("Не удалось подключиться к серверу")

    def show_error(self, message):
        QMessageBox.warning(self.auth_app, "Ошибка", message)

    def show_register(self):
        self.auth_app.login_form.clear_inputs()
        self.auth_app.stacked_widget.setCurrentWidget(self.auth_app.register_form)
        self.auth_app.setWindowTitle("Авторизация")
