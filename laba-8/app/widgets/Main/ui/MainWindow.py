from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QSpacerItem,
    QSizePolicy,
    QComboBox,
    QLineEdit,
    QMessageBox,
)
from PyQt5.QtCore import Qt
from fractions import Fraction


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

        # Калькулятор дробей
        self.init_fraction_calculator(layout)

        # Разделитель
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(spacer)

        # Кнопка выхода
        self.logout_button = QPushButton("Выйти")
        self.logout_button.setStyleSheet("background-color: #f44336; color: white;")
        self.logout_button.clicked.connect(self.logic_handler.handle_logout)
        layout.addWidget(self.logout_button)

        self.setLayout(layout)

    def init_fraction_calculator(self, layout):
        # Заголовок калькулятора
        calc_label = QLabel("Калькулятор дробей")
        calc_label.setAlignment(Qt.AlignCenter)
        calc_label.setStyleSheet("font-size: 18px; font-weight: bold;")
        layout.addWidget(calc_label)

        # Первое число
        self.num1_layout = QHBoxLayout()
        self.num1_type = QComboBox()
        self.num1_type.addItems(["Обыкновенная дробь", "Десятичная дробь"])
        self.num1_type.currentIndexChanged.connect(self.update_num1_fields)

        self.num1_numerator = QLineEdit()
        self.num1_denominator = QLineEdit()

        self.num1_layout.addWidget(self.num1_type)
        self.num1_layout.addWidget(self.num1_numerator)
        self.num1_layout.addWidget(QLabel("/"))
        self.num1_layout.addWidget(self.num1_denominator)
        layout.addLayout(self.num1_layout)

        # Второе число
        self.num2_layout = QHBoxLayout()
        self.num2_type = QComboBox()
        self.num2_type.addItems(["Обыкновенная дробь", "Десятичная дробь"])
        self.num2_type.currentIndexChanged.connect(self.update_num2_fields)

        self.num2_numerator = QLineEdit()
        self.num2_denominator = QLineEdit()

        self.num2_layout.addWidget(self.num2_type)
        self.num2_layout.addWidget(self.num2_numerator)
        self.num2_layout.addWidget(QLabel("/"))
        self.num2_layout.addWidget(self.num2_denominator)
        layout.addLayout(self.num2_layout)

        # Кнопка сравнения
        compare_btn = QPushButton("Сравнить")
        compare_btn.clicked.connect(self.compare_fractions)
        compare_btn.setStyleSheet("background-color: #4CAF50; color: white;")
        layout.addWidget(compare_btn)

        # Результат
        self.result_label = QLabel("")
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.setStyleSheet("font-size: 16px;")
        layout.addWidget(self.result_label)

    def update_num1_fields(self):
        if self.num1_type.currentText() == "Десятичная дробь":
            self.num1_denominator.hide()
            self.num1_layout.itemAt(2).widget().hide()
        else:
            self.num1_denominator.show()
            self.num1_layout.itemAt(2).widget().show()

    def update_num2_fields(self):
        if self.num2_type.currentText() == "Десятичная дробь":
            self.num2_denominator.hide()
            self.num2_layout.itemAt(2).widget().hide()
        else:
            self.num2_denominator.show()
            self.num2_layout.itemAt(2).widget().show()

    def compare_fractions(self):
        try:
            # Получаем первое число
            if self.num1_type.currentText() == "Десятичная дробь":
                num1 = float(self.num1_numerator.text())
            else:
                num1 = Fraction(
                    int(self.num1_numerator.text()), int(self.num1_denominator.text())
                )

            # Получаем второе число
            if self.num2_type.currentText() == "Десятичная дробь":
                num2 = float(self.num2_numerator.text())
            else:
                num2 = Fraction(
                    int(self.num2_numerator.text()), int(self.num2_denominator.text())
                )

            # Сравниваем
            if num1 < num2:
                result = f"{num1} < {num2}"
            elif num1 > num2:
                result = f"{num1} > {num2}"
            else:
                result = f"{num1} = {num2}"

            self.result_label.setText(result)

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные числа")
        except ZeroDivisionError:
            QMessageBox.warning(self, "Ошибка", "Знаменатель не может быть нулём")

    def set_user_info(self, username):
        self.welcome_label.setText("Добро пожаловать!")
        self.user_info_label.setText(f"Вы вошли как: {username}")
