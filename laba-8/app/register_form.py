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


class RegisterForm(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        
        super().resize(1000, 1000)

    def init_ui(self):
        layout = QVBoxLayout()

        # Заголовок
        title_label = QLabel("Регистрация")
        layout.addWidget(title_label)

        # Поля ввода
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Логин")
        layout.addWidget(self.username_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_input)

        # Кнопка регистрации
        self.register_button = QPushButton("Зарегистрироваться")
        
        self.register_button.setStyleSheet("background-color: #454545; color: white;")
        layout.addWidget(self.register_button)

        # Разделитель
        spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Кнопка возврата
        self.back_button = QPushButton("Назад к авторизации")
        self.back_button.setStyleSheet("color: #454545; border: none;")
        layout.addWidget(self.back_button)

        self.setLayout(layout)
