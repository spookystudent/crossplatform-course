# 6. Модуль tkinter  

Модуль tkinter  
Многие программы на сегодняшний день используют графический интерфейс, который более интуитивен и удобен для пользователя, чем консоль.  

Модуль Tkinter предназначен для работы с компонентами графического интерфейса пользователя (graphical user interface – GUI).  

Tkinter доступен в виде отдельного встроенного модуля, который содержит все необходимые графические компоненты – кнопки, текстовые поля и т.д.  

Как и любой модуль, tkinter в Python можно импортировать:  
```python
from tkinter import *
```

Модуль tkinter  
tkinter – графический модуль, который входит в стандартный комплект Python и позволяет программировать не только в объектном, но и в процедурном стиле.  

Примеры импорта:  
```python
import tkinter  
tk = tkinter.Tk()  
```  
или  
```python
from tkinter import *  
tk = Tk()  
```

### Tcl/Tk  
Скриптовый язык Tcl (от англ. Tool Command Language) разработан в 1988 году Джоном Оустерхаутом, который в то время работал в университете Бэркли.  

Язык состоит из команд и их параметров, разделенных пробелами. Все данные – текстовые. Ключевых слов нет.  

Tk – графическая библиотека, написанная для Tcl.  

Области применения языка:  
- быстрое прототипирование,  
- создание графических интерфейсов для консольных программ,  
- встраивание в прикладные программы,  
- тестирование,  
- системная интеграция.  

### Главное окно  
```python
import tkinter  
from tkinter import *  

root = Tk()  
root.mainloop()  
```  

Конструктор – функция, которая создает и возвращает объект.  
Объект – то, что имеет методы.  
`tk` – объект главного окна.  

Вместе с созданием главного окна запускается цикл обработки сообщений. Сообщения поступают в программу от пользователя и от операционной системы.  

### Создание окна  
Базовым моментом в построении графических программ является создание окна. Затем в окно добавляются все остальные компоненты графического интерфейса.  

### Окно с кнопкой  
```python
import tkinter  
from tkinter import *  

root = Tk()  
btn1 = Button(root)  
btn1["text"] = 'Превед'  
btn1["bg"] = 'blue'  
btn1["fg"] = 'white'  
btn1.place(x=100, y=50)  

btn2 = Button(root, text='Медвед', bg='blue', fg='white')  
btn2.place(x=200, y=50)  

root.mainloop()  
```  

### Задание свойств виджета  
Задавать свойства виджета можно тремя способами:  
1. Во время создания объекта с помощью именованных параметров:  
   ```python
   btn1 = Button(root, text='Привет', bg='blue', fg='white')  
   ```  
2. После создания объекта, рассматривая объекты как словари, а название опции как ключ:  
   ```python
   btn1["text"] = 'Привет'  
   btn1["bg"] = 'blue'  
   btn1["fg"] = 'white'  
   ```  
3. После создания объекта при помощи его метода `config()`:  
   ```python
   btn1.config(text='Привет', bg='blue', fg='white')  
   ```  

### Правильное проектирование  
Принцип проектирования "Разделение ответственности": один модуль решает одну задачу.  

Есть две задачи:  
- построение GUI,  
- выполнение расчетов.  

Вывод: должно быть два модуля.  

### Метки  
Метки (или надписи) содержат строку (или несколько строк) текста и служат для информирования пользователя.  

Пример:  
```python
label1 = Label(root, text="Это метка!\nИз двух строк.", font="Arial 18")  
label1.place(x=0, y=0)  
```  

Виджеты (управляющие элементы) – видимые объекты, воспринимающие действия пользователя и передающие информацию ему.  

### Текстовое поле  
В него пользователь может ввести только одну строку текста.  

Пример:  
```python
entry = Entry(root, width=20, bd=3)  
```  
- `width` – ширина поля в символах.  
- `bd` – ширина границы.  

### Многострочное текстовое поле  
Позволяет ввести несколько строк текста.  

Пример:  
```python
text = Text(root, width=30, height=5, font="Verdana 12", wrap=WORD)  
```  

Свойство `wrap` определяет перенос текста:  
- `WORD` – по словам.  
- `CHAR` – по символам.  
- `NONE` – без переноса.  

### "Переменные" библиотеки tkinter  
Переменные – это объекты, которые дают дополнительные возможности для управления виджетами.  

Типы переменных:  
- `StringVar()` – строковые.  
- `IntVar()` – целые.  
- `DoubleVar()` – вещественные.  
- `BooleanVar()` – логические.  

Методы переменных:  
- `set()` – установка значения.  
- `get()` – получение значения.  

Пример:  
```python
v = StringVar()  
v.set("Привет!")  
ent = Entry(root, width=20, bd=3, textvariable=v)  
```  

Одну переменную можно связать с несколькими виджетами.  

### Радиокнопки (переключатели)  
Радиокнопка никогда не используется в одиночку. Их используют группами, при этом в одной группе может быть «включена» лишь одна кнопка.  

Пример:  
```python
var1 = IntVar()  
var1.set(1)  
var2 = IntVar()  
var2.set(0)  

# Первая группа  
r1 = Radiobutton(root, text="Первая", variable=var1, value=0)  
r2 = Radiobutton(root, text="Вторая", variable=var1, value=1)  

# Вторая группа  
r3 = Radiobutton(root, text="Третья", variable=var2, value=0)  
r4 = Radiobutton(root, text="Четвертая", variable=var2, value=1)  
```  

### Флажки  
Объект `Checkbutton` предназначен для выбора одного и более не взаимоисключающих пунктов.  

Пример:  
```python
v1 = IntVar()  
v2 = IntVar()  

check1 = Checkbutton(root, text="Первый флажок", variable=v1, onvalue=1, offvalue=0)  
check2 = Checkbutton(root, text="Второй флажок", variable=v2, onvalue=5, offvalue=0)  
```  

### Списки  
`Listbox` – это объект, в котором пользователь может выбрать один или несколько пунктов.  

Пример:  
```python
words = ['Linux', 'Python', 'Tk', 'Tkinter']  
listbox = Listbox(root, selectmode=SINGLE, height=4)  

# Заполнение списка  
for i in words:  
    listbox.insert(END, i)  
```  

Получить выбранную строку можно методом `listbox.selection_get()`.  

### Менеджеры расположения  
При изменении размеров главного окна все его дочерние виджеты должны подстроиться под новые размеры родителя.  

В библиотеке tkinter их три:  
1. `grid` – табличное расположение.  
2. `pack` – автоматическое расположение.  
3. `place` – абсолютное расположение.  

#### Пример с `place`:  
```python
import tkinter  
from tkinter import *  

root = Tk()  
entry = Entry(root, width=25)  
entry.place(x=20, y=20)  

lbl = Label(root, text='= 1000')  
lbl.place(x=200, y=20)  

btn = Button(root, text='Вычислить')  
btn.place(x=20, y=50)  

root.mainloop()  
```  

#### Пример с `pack`:  
```python
import tkinter  
from tkinter import *  

root = Tk()  
entry = Entry(root, width=25)  
entry.pack()  

lbl = Label(root, text='= 1000')  
lbl.pack()  

btn = Button(root, text='Вычислить')  
btn.pack()  

root.mainloop()  
```  

#### Пример с `grid`:  
```python
import tkinter  
from tkinter import *  

root = Tk()  
entry = Entry(root, width=25)  
entry.grid(row=0, column=0, padx=5, pady=5)  

lbl = Label(root, text='= 1000', bg='gray')  
lbl.grid(row=0, column=1, padx=5, pady=5)  

btn = Button(root, text='Вычислить')  
btn.grid(row=1, column=0, columnspan=2)  

root.mainloop()  
```  

### События  
Типовой сценарий события:  
1. Пользователь совершил действие (кликнул мышкой по кнопке).  
2. Операционная система получила информацию об этом.  
3. ОС вычислила программу и кнопку, по которой кликнул пользователь.  
4. ОС отправила сообщение программе с информацией о действии пользователя.  
5. Программа вызывает функцию, связанную с этим событием.  

#### Метод `bind()`  
Метод `bind()` привязывает функцию к какому-либо действию пользователя.  

Пример:  
```python
from tkinter import *  

root = Tk()  
frm = Frame(root, width=400, height=400, bg="pink")  
frm.pack()  

def my(e):  
    b = Button(frm, text="XXX")  
    b.place(x=e.x, y=e.y)  

frm.bind("<Button-1>", my)  
root.mainloop()  
```  

#### Виды событий:  
- `MouseWheel` – прокрутка колесом мыши.  
- `KeyPress`, `KeyRelease` – нажатие и отпускание клавиши.  
- `ButtonPress`, `ButtonRelease`, `Motion` – действия с мышью.  
- `Configure` – изменение размера окна.  
- `FocusIn`, `FocusOut` – получение или потеря фокуса.  
- `Enter`, `Leave` – вход или выход курсора мыши из виджета.  

### Объекты класса Canvas  
Для рисования простейших рисунков создаются объекты-холсты.  

Пример:  
```python
c = Canvas(root, width=200, height=200, bg='white')  
c.pack()  
```  

#### Методы для рисования:  
- `create_line()` – линия.  
- `create_rectangle()` – прямоугольник.  
- `create_polygon()` – многоугольник.  
- `create_oval()` – овал или круг.  
- `create_arc()` – дуга.  
- `create_text()` – текст.  

Пример линии:  
```python
c.create_line(10, 10, 100, 50, fill='red')  
```  

Пример прямоугольника:  
```python
c.create_rectangle(50, 50, 150, 150, fill='blue')  
```  

Пример круга:  
```python
c.create_oval(50, 50, 150, 150, fill='green')  
```  

### Самостоятельные задания  
1. Создать окно с тремя кнопками: "Красный", "Зеленый", "Синий". При нажатии на кнопку окно должно окрашиваться в соответствующий цвет.  
2. Реализовать игру "Крестики-нолики" на поле 3x3.  

#### Пример решения для кнопок:  
```python
from tkinter import *  

tk = Tk()  

def paint(color):  
    tk.config(bg=color)  

buttons = [  
    Button(tk, text="Red", command=lambda: paint("red")),  
    Button(tk, text="Green", command=lambda: paint("green")),  
    Button(tk, text="Blue", command=lambda: paint("blue")),  
]  

for b in buttons:  
    b.pack(side=LEFT)  

tk.mainloop()  
