from PyQt5.QtWidgets import QMessageBox




class MainLogic:
    
    def __init__(self, auth_app):
        from core.app import AuthApp
        self.auth_app: 'AuthApp' = auth_app

    def handle_logout(self):
        reply = QMessageBox.question(
            self.auth_app.main_window,
            "Подтверждение",
            "Вы действительно хотите выйти?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No,
        )

        if reply == QMessageBox.Yes:
            self.perform_logout()

    def perform_logout(self):
        self.auth_app.AUTH_TOKEN = None
        self.auth_app.login_form.clear_inputs()
        self.auth_app.register_form.logic_handler.show_login_form()
