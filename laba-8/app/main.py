import sys
import requests
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
    QMessageBox,
    QDialog,
)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices

# Импортируем наши формы
from login_form import LoginForm
from register_form import RegisterForm


BASE_API_URL = "http://127.0.0.1:5000/"


class AuthApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        self.setFixedSize(380, 140)

        # Создаем стек виджетов для переключения между формами
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)

        # Создаем экземпляры форм
        self.login_form = LoginForm()
        self.register_form = RegisterForm()
        self.main_window = MainWindow()

        # Добавляем формы в стек
        self.stacked_widget.addWidget(self.login_form)
        self.stacked_widget.addWidget(self.register_form)
        self.stacked_widget.addWidget(self.main_window)

        # Подключаем сигналы
        self.login_form.register_button.clicked.connect(self.show_register_form)
        self.login_form.login_button.clicked.connect(self.handle_login)

        self.register_form.back_button.clicked.connect(self.show_login_form)
        self.register_form.register_button.clicked.connect(self.handle_register)

        self.main_window.logout_button.clicked.connect(self.logout)


    def show_register_form(self):
        self.stacked_widget.setCurrentWidget(self.register_form)
        self.setWindowTitle("Регистрация")

    def show_login_form(self):
        self.stacked_widget.setCurrentWidget(self.login_form)
        self.setWindowTitle("Авторизация")

    def show_main_window(self):
        self.stacked_widget.setCurrentWidget(self.main_window)
        self.setWindowTitle("Главное окно")

    def handle_login(self):
        name = self.login_form.name_input.text()
        password = self.login_form.password_input.text()

        if not name or not password:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        try:
            response = requests.post(
                f"{BASE_API_URL}/auth/login",
                json={"name": name, "password": password},
            )

            if response.status_code == 200:
                data = response.json()
                self.main_window.set_user_info(name)
                self.show_main_window()
            else:
                QMessageBox.warning(
                    self,
                    "Ошибка",
                    response.json().get("message", "Неверные учетные данные"),
                )

        except requests.exceptions.RequestException:
            QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к серверу")

    def handle_register(self):
        name = self.register_form.name_input.text()
        password = self.register_form.password_input.text()

        if not name or not password:
            QMessageBox.warning(self, "Ошибка", "Заполните все поля")
            return

        try:
            response = requests.post(
                f"{BASE_API_URL}/auth/register",
                json={"name": name, "password": password},
            )

            if response.status_code == 201:
                QMessageBox.information(self, "Успех", "Регистрация прошла успешно")
                self.show_login_form()
            else:
                print(response.json())
                QMessageBox.warning(
                    self, "Ошибка", str(response.json())
                )

        except requests.exceptions.RequestException:
            QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к серверу")

    def logout(self):
        self.login_form.clear_inputs()
        self.show_login_form()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Устанавливаем стиль для красивого отображения
    app.setStyle("Fusion")

    window = AuthApp()
    window.show()
    sys.exit(app.exec_())
