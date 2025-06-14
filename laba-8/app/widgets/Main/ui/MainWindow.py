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
            if hasattr(self, 'result_container'):
                self.result_container.deleteLater()
            
            self.result_container = QWidget()
            result_layout = QHBoxLayout()
            result_layout.setAlignment(Qt.AlignCenter)
            self.result_container.setLayout(result_layout)
            
            if self.num1_type.currentText() == "Десятичная дробь":
                num1 = float(self.num1_numerator.text())
                num1_widget = QLabel(str(num1))
                num1_widget.setAlignment(Qt.AlignCenter)
                result_layout.addWidget(num1_widget)
            else:
                numerator1 = int(self.num1_numerator.text())
                denominator1 = int(self.num1_denominator.text())
                num1 = Fraction(numerator1, denominator1)
                
                num1_layout = QVBoxLayout()
                num1_layout.setSpacing(0)
                
                num_label = QLabel(str(numerator1))
                num_label.setAlignment(Qt.AlignCenter)
                line_label = QLabel("—")
                line_label.setAlignment(Qt.AlignCenter)
                denom_label = QLabel(str(denominator1))
                denom_label.setAlignment(Qt.AlignCenter)
                
                num1_layout.addWidget(num_label)
                num1_layout.addWidget(line_label)
                num1_layout.addWidget(denom_label)
                
                num1_widget = QWidget()
                num1_widget.setLayout(num1_layout)
                result_layout.addWidget(num1_widget)

            if self.num2_type.currentText() == "Десятичная дробь":
                num2 = float(self.num2_numerator.text())
                num2_widget = QLabel(str(num2))
                num2_widget.setAlignment(Qt.AlignCenter)
            else:
                numerator2 = int(self.num2_numerator.text())
                denominator2 = int(self.num2_denominator.text())
                num2 = Fraction(numerator2, denominator2)
                
                num2_layout = QVBoxLayout()
                num2_layout.setSpacing(0)
                
                num_label = QLabel(str(numerator2))
                num_label.setAlignment(Qt.AlignCenter)
                line_label = QLabel("—")
                line_label.setAlignment(Qt.AlignCenter)
                denom_label = QLabel(str(denominator2))
                denom_label.setAlignment(Qt.AlignCenter)
                
                num2_layout.addWidget(num_label)
                num2_layout.addWidget(line_label)
                num2_layout.addWidget(denom_label)
                
                num2_widget = QWidget()
                num2_widget.setLayout(num2_layout)

            if num1 < num2:
                comparison = "<"
            elif num1 > num2:
                comparison = ">"
            else:
                comparison = "="
            

            comparison_label = QLabel(comparison)
            comparison_label.setAlignment(Qt.AlignCenter)
            comparison_label.setStyleSheet("font-size: 16px; margin: 0 10px;")
            
            result_layout.addWidget(comparison_label)
            result_layout.addWidget(num2_widget)
            

            if hasattr(self, 'result_label'):
                self.layout().replaceWidget(self.result_label, self.result_container)
                self.result_label.deleteLater()
            else:
                self.layout().addWidget(self.result_container)
            

            self.result_label = self.result_container

        except ValueError:
            QMessageBox.warning(self, "Ошибка", "Пожалуйста, введите корректные числа")
        except ZeroDivisionError:
            QMessageBox.warning(self, "Ошибка", "Знаменатель не может быть нулём")

    def set_user_info(self, username):
        self.welcome_label.setText("Добро пожаловать!")
        self.user_info_label.setText(f"Вы вошли как: {username}")
