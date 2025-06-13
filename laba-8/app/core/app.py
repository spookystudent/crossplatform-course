from PyQt5.QtWidgets import QMainWindow, QStackedWidget, QMessageBox

from widgets.Main.ui import MainWindow
from widgets.Auth.ui import RegisterForm, LoginForm


from typing import List, Union


class AuthApp(QMainWindow):
    BASE_API_URL = "http://127.0.0.1:5000/"

    AUTH_TOKEN: str = None

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Авторизация")
        # self.setFixedSize(640, 140)

        self.main_window = MainWindow(self)
        self.login_form = LoginForm(self)
        self.register_form = RegisterForm(self)
        
        self.init_widgets()



    def init_widgets(self):
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)


        self.stacked_widget.addWidget(self.login_form)
        self.stacked_widget.addWidget(self.register_form)
        self.stacked_widget.addWidget(self.main_window)

    def show_main_window(self):
        self.stacked_widget.setCurrentWidget(self.main_window)
        self.setWindowTitle("Главное окно")

