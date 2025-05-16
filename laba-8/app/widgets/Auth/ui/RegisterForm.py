from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QSpacerItem,
    QSizePolicy,
)
from PyQt5.QtCore import Qt

from ..logic import RegisterLogic


class RegisterForm(QWidget):
    def __init__(self, instance):
        super().__init__()
        self.logic_handler = RegisterLogic(instance)
        self.init_ui()


    def clear_inputs(self):
        """Очистка полей ввода"""
        self.name_input.clear()
        self.password_input.clear()


    #* _____________________________________________________________________
    #* | Init    
    #* - UI
    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок
        title_label = QLabel("Регистрация")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 20px; font-weight: bold;")
        layout.addWidget(title_label)

        # Поля ввода
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Логин")
        layout.addWidget(self.name_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Кнопка регистрации
        self.register_button = QPushButton("Зарегистрироваться")
        self.register_button.clicked.connect(self.logic_handler.handle_register)

        self.register_button.setStyleSheet("background-color: #454545; color: white;")
        layout.addWidget(self.register_button)

        # Разделитель
        spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Кнопка возврата
        self.login_button = QPushButton("Назад к авторизации")
        self.login_button.setStyleSheet("color: #454545; border: none;")
        self.login_button.clicked.connect(self.logic_handler.show_login_form)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    #* |__________________________________________________________________________
