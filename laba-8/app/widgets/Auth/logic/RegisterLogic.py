from PyQt5.QtWidgets import QMessageBox



import requests


class RegisterLogic:
    def __init__(self, auth_app):
        from core.app import AuthApp
        self.auth_app: 'AuthApp' = auth_app
        self.base_api_url = self.auth_app.BASE_API_URL

    def handle_register(self):
        name = self.auth_app.register_form.name_input.text()
        password = self.auth_app.register_form.password_input.text()
        if not name or not password:
            self.show_error("Заполните все поля")
            return

        try:
            response = requests.post(
                f"{self.base_api_url}/auth/register",
                json={"name": name, "password": password},
            )

            if response.status_code == 201:
                self.on_register_success()
            else:
                self.on_register_failure(response)

        except requests.exceptions.RequestException:
            self.on_connection_error()

    def on_register_success(self):
        """Действия при успешной регистрации"""
        QMessageBox.information(
            self.auth_app.register_form, "Успех", "Регистрация прошла успешно"
        )
        self.auth_app.register_form.clear_inputs()
        self.show_login_form()

    def on_register_failure(self, response):
        """Действия при ошибке регистрации"""
        error_message = str(response.json())
        self.show_error(error_message)

    def on_connection_error(self):
        """Действия при ошибке соединения"""
        self.show_error("Не удалось подключиться к серверу")

    def show_login_form(self):
        """Обработка нажатия кнопки перехода к регистрации"""
        self.auth_app.register_form.clear_inputs()
        self.auth_app.stacked_widget.setCurrentWidget(self.auth_app.login_form)
        self.auth_app.setWindowTitle("Авторизация")

    def show_error(self, message):
        """Показать сообщение об ошибке"""
        QMessageBox.warning(self.auth_app, "Ошибка", message)
