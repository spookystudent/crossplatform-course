# 7. PYQT
PYQT - это инструментарий виджетов GUI. Это интерфейс Python для Qt, одна из самых мощных и популярных кросс-платформенных библиотек GUI. Разработан компанией Riverbank Computing Ltd.

PYQT API - это набор модулей, содержащих большое количество классов и функций. API (Application Programming Interface) - набор способов и правил для взаимодействия программ.

Основные модули:

1. QtCore - ядро с неграфической функциональностью
2. QtGui - классы для интеграции окон, обработки событий, 2D-графики
3. QtWidgets - UI-элементы для классических интерфейсов
4. QtMultimedia - управление мультимедиа, доступ к камере
5. QtNetwork - сетевое программирование
6. QtWebKit - реализация веб-браузера
7. QtSql - работа с базами данных

Основные типы данных:
- QString - Unicode-строка
- QChar - Unicode-символ
- QByteArray - массив байтов
- QVariant - может хранить данные любого типа

Создание простого окна:

```python
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

app = QApplication([])
window = QWidget()
label = QLabel("Hello PyQt!", parent=window)
window.show()
app.exec_()
```

Основные компоненты:
- QLabel - текстовая метка
- QPushButton - кнопка
- QLineEdit - поле ввода
- QTextEdit - многострочный редактор
- QRadioButton - переключатель
- QCheckBox - флажок

Менеджеры компоновки:
- QHBoxLayout - горизонтальное расположение
- QVBoxLayout - вертикальное расположение 
- QGridLayout - расположение в сетке

Главные классы окон:
- QWidget - базовый виджет
- QMainWindow - главное окно с меню и панелями
- QDialog - диалоговое окно

PYQT предоставляет мощные инструменты для создания кросс-платформенных приложений с графическим интерфейсом на Python.
