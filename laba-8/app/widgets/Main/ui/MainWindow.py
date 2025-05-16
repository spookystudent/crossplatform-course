from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QSpacerItem,
    QSizePolicy,
)
from PyQt5.QtCore import Qt


from ..logic import MainLogic

class MainWindow(QWidget):

    def __init__(self, instance):
        super().__init__()
        self.logic_handler = MainLogic(instance)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Приветствие
        self.welcome_label = QLabel("Добро пожаловать!")
        self.welcome_label.setAlignment(Qt.AlignCenter)
        self.welcome_label.setStyleSheet("font-size: 24px; font-weight: bold;")
        layout.addWidget(self.welcome_label)

        # Информация о пользователе
        self.user_info_label = QLabel()
        self.user_info_label.setAlignment(Qt.AlignCenter)
        self.user_info_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.user_info_label)

        # Разделитель
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Кнопка выхода
        self.logout_button = QPushButton("Выйти")
        self.logout_button.setStyleSheet("background-color: #f44336; color: white;")
        self.logout_button.clicked.connect(self.logic_handler.handle_logout)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def set_user_info(self, username):
        self.welcome_label.setText(f"Добро пожаловать, {username}!")
        self.user_info_label.setText(f"Вы вошли как: {username}")
