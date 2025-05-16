from PyQt5.QtWidgets import QApplication
import sys


if __name__ == "__main__":
    from core.app import AuthApp

    app = QApplication(sys.argv)

    AuthApp().show()

    sys.exit(app.exec_())