import tkinter as tk
from tkinter import messagebox, ttk
from fractions import Fraction


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор дробей с аутентификацией")
        self.users = {}
        self.current_user = None
        self.show_login_frame()

    def show_login_frame(self):
        self.clear_frame()
        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack(padx=20, pady=20)
        tk.Label(self.login_frame, text="Логин:").grid(row=0, column=0, sticky="e")
        self.login_entry = tk.Entry(self.login_frame)
        self.login_entry.grid(row=0, column=1, pady=5)
        tk.Label(self.login_frame, text="Пароль:").grid(row=1, column=0, sticky="e")
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=1, column=1, pady=5)
        tk.Button(self.login_frame, text="Войти", command=self.login).grid(
            row=2, column=1, pady=5, sticky="e"
        )
        tk.Button(
            self.login_frame, text="Регистрация", command=self.show_register_frame
        ).grid(row=2, column=0, pady=5, sticky="w")

    def show_register_frame(self):
        self.clear_frame()
        self.register_frame = tk.Frame(self.root)
        self.register_frame.pack(padx=20, pady=20)

        tk.Label(self.register_frame, text="Логин:").grid(row=0, column=0, sticky="e")
        self.reg_login_entry = tk.Entry(self.register_frame)
        self.reg_login_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.register_frame, text="Пароль:").grid(row=1, column=0, sticky="e")
        self.reg_password_entry = tk.Entry(self.register_frame, show="*")
        self.reg_password_entry.grid(row=1, column=1, pady=5)

        tk.Label(self.register_frame, text="Повторите пароль:").grid(
            row=2, column=0, sticky="e"
        )
        self.reg_confirm_entry = tk.Entry(self.register_frame, show="*")
        self.reg_confirm_entry.grid(row=2, column=1, pady=5)

        tk.Button(
            self.register_frame, text="Зарегистрироваться", command=self.register
        ).grid(row=3, column=1, pady=5, sticky="e")
        tk.Button(
            self.register_frame, text="Назад", command=self.show_login_frame
        ).grid(row=3, column=0, pady=5, sticky="w")

    def show_calculator_frame(self):
        self.clear_frame()
        self.calculator_frame = tk.Frame(self.root)
        self.calculator_frame.pack(padx=20, pady=20)
        tk.Label(
            self.calculator_frame,
            text=f"Добро пожаловать, {self.current_user}!\nКалькулятор сравнения дробей",
            font=("Arial", 12),
        ).grid(row=0, column=0, columnspan=4, pady=10)
        tk.Label(self.calculator_frame, text="Первое число:").grid(
            row=1, column=0, sticky="e"
        )
        self.fraction_type1 = ttk.Combobox(
            self.calculator_frame,
            values=["Обыкновенная дробь", "Десятичная дробь"],
            state="readonly",
        )
        self.fraction_type1.grid(row=1, column=1, pady=5, padx=5)
        self.fraction_type1.current(0)
        self.fraction_type1.bind("<<ComboboxSelected>>", self.update_input_fields)
        self.fraction_frame1 = tk.Frame(self.calculator_frame)
        self.fraction_frame1.grid(row=1, column=2, columnspan=2)
        self.numerator1 = tk.Entry(self.fraction_frame1, width=5)
        self.numerator1.pack(side=tk.LEFT)
        tk.Label(self.fraction_frame1, text="/").pack(side=tk.LEFT)
        self.denominator1 = tk.Entry(self.fraction_frame1, width=5)
        self.denominator1.pack(side=tk.LEFT)
        tk.Label(self.calculator_frame, text="Второе число:").grid(
            row=2, column=0, sticky="e"
        )
        self.fraction_type2 = ttk.Combobox(
            self.calculator_frame,
            values=["Обыкновенная дробь", "Десятичная дробь"],
            state="readonly",
        )
        self.fraction_type2.grid(row=2, column=1, pady=5, padx=5)
        self.fraction_type2.current(0)
        self.fraction_type2.bind("<<ComboboxSelected>>", self.update_input_fields)
        self.fraction_frame2 = tk.Frame(self.calculator_frame)
        self.fraction_frame2.grid(row=2, column=2, columnspan=2)
        self.numerator2 = tk.Entry(self.fraction_frame2, width=5)
        self.numerator2.pack(side=tk.LEFT)
        tk.Label(self.fraction_frame2, text="/").pack(side=tk.LEFT)
        self.denominator2 = tk.Entry(self.fraction_frame2, width=5)
        self.denominator2.pack(side=tk.LEFT)
        tk.Button(
            self.calculator_frame, text="Сравнить", command=self.compare_fractions
        ).grid(row=3, column=1, pady=10)
        self.result_label = tk.Label(self.calculator_frame, text="", font=("Arial", 12))
        self.result_label.grid(row=4, column=0, columnspan=4)
        tk.Button(self.calculator_frame, text="Выйти", command=self.logout).grid(
            row=5, column=0, columnspan=4, pady=10
        )

    def update_input_fields(self, event=None):
        if self.fraction_type1.get() == "Десятичная дробь":
            self.fraction_frame1.destroy()
            self.fraction_frame1 = tk.Frame(self.calculator_frame)
            self.fraction_frame1.grid(row=1, column=2)
            self.numerator1 = tk.Entry(self.fraction_frame1, width=10)
            self.numerator1.pack()
            self.denominator1 = None
        else:
            self.fraction_frame1.destroy()
            self.fraction_frame1 = tk.Frame(self.calculator_frame)
            self.fraction_frame1.grid(row=1, column=2, columnspan=2)
            self.numerator1 = tk.Entry(self.fraction_frame1, width=5)
            self.numerator1.pack(side=tk.LEFT)
            tk.Label(self.fraction_frame1, text="/").pack(side=tk.LEFT)
            self.denominator1 = tk.Entry(self.fraction_frame1, width=5)
            self.denominator1.pack(side=tk.LEFT)
        if self.fraction_type2.get() == "Десятичная дробь":
            self.fraction_frame2.destroy()
            self.fraction_frame2 = tk.Frame(self.calculator_frame)
            self.fraction_frame2.grid(row=2, column=2)
            self.numerator2 = tk.Entry(self.fraction_frame2, width=10)
            self.numerator2.pack()
            self.denominator2 = None
        else:
            self.fraction_frame2.destroy()
            self.fraction_frame2 = tk.Frame(self.calculator_frame)
            self.fraction_frame2.grid(row=2, column=2, columnspan=2)
            self.numerator2 = tk.Entry(self.fraction_frame2, width=5)
            self.numerator2.pack(side=tk.LEFT)
            tk.Label(self.fraction_frame2, text="/").pack(side=tk.LEFT)
            self.denominator2 = tk.Entry(self.fraction_frame2, width=5)
            self.denominator2.pack(side=tk.LEFT)

    def compare_fractions(self):
        try:
            if self.fraction_type1.get() == "Десятичная дробь":
                num1 = float(self.numerator1.get())
            else:
                num1 = Fraction(
                    int(self.numerator1.get()), int(self.denominator1.get())
                )
            if self.fraction_type2.get() == "Десятичная дробь":
                num2 = float(self.numerator2.get())
            else:
                num2 = Fraction(
                    int(self.numerator2.get()), int(self.denominator2.get())
                )
            if num1 < num2:
                result = f"{num1} < {num2}"
            elif num1 > num2:
                result = f"{num1} > {num2}"
            else:
                result = f"{num1} = {num2}"
            self.result_label.config(text=result)
        except ValueError:
            messagebox.showerror("Ошибка", "Пожалуйста, введите корректные числа")
        except ZeroDivisionError:
            messagebox.showerror("Ошибка", "Знаменатель не может быть нулём")

    def clear_frame(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def register(self):
        login = self.reg_login_entry.get()
        password = self.reg_password_entry.get()
        confirm = self.reg_confirm_entry.get()
        if not login or not password:
            messagebox.showerror("Ошибка", "Логин и пароль не могут быть пустыми")
            return
        if password != confirm:
            messagebox.showerror("Ошибка", "Пароли не совпадают")
            return
        if login in self.users:
            messagebox.showerror(
                "Ошибка", "Пользователь с таким логином уже существует"
            )
            return
        self.users[login] = password
        messagebox.showinfo("Успех", "Регистрация прошла успешно!")
        self.show_login_frame()

    def login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        if not login or not password:
            messagebox.showerror("Ошибка", "Введите логин и пароль")
            return
        if login not in self.users or self.users[login] != password:
            messagebox.showerror("Ошибка", "Неверный логин или пароль")
            return
        self.current_user = login
        self.show_calculator_frame()

    def logout(self):
        self.current_user = None
        self.show_login_frame()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
