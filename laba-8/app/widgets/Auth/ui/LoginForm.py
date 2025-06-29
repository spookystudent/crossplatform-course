from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, 
    QPushButton, QSpacerItem, QSizePolicy
)
from PyQt5.QtCore import Qt

from ..logic import LoginLogic

class LoginForm(QWidget):
    def __init__(self, instance):
        super().__init__()
        self.logic_handler = LoginLogic(instance)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок
        title_label = QLabel("Авторизация")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title_label)

        # Поля ввода
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Имя пользователя")
        layout.addWidget(self.name_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Кнопка входа
        self.login_button = QPushButton("Войти")
        self.login_button.setStyleSheet("background-color: #454545; color: white;")
        self.login_button.clicked.connect(self.logic_handler.handle_login)
        layout.addWidget(self.login_button)

        # Разделитель
        spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Кнопка регистрации
        self.register_button = QPushButton("Нет аккаунта? Зарегистрироваться")
        self.register_button.setStyleSheet("color: #454545; border: none;")
        self.register_button.clicked.connect(self.logic_handler.show_register)
        layout.addWidget(self.register_button)

        self.setLayout(layout)

    def clear_inputs(self):
        """Очистка полей ввода"""
        self.name_input.clear()
        self.password_input.clear()