import tkinter as tk
from tkinter import ttk

class PrimeGenerator:
    def __init__(self):
        self.primes = []
        self.current = 1
    
    def next_prime(self):
        while True:
            self.current += 1
            if self.is_prime(self.current):
                self.primes.append(self.current)
                return self.current
    
    def is_prime(self, n):
        if n <= 1:
            return False
        for p in self.primes:
            if p * p > n:
                break
            if n % p == 0:
                return False
        return True

class FibonacciGenerator:
    def __init__(self):
        self.a, self.b = 0, 1
        self.count = 0
    
    def next_fibonacci(self):
        self.count += 1
        if self.count == 1:
            return 1
        self.a, self.b = self.b, self.a + self.b
        return self.b

class MersennePrimeGenerator:
    def __init__(self):
        self.n = 0
        self.prime_gen = PrimeGenerator()
    
    def next_mersenne_prime(self):
        while True:
            self.n += 1
            mersenne = 2 ** self.n - 1
            if self.prime_gen.is_prime(mersenne):
                return mersenne

class Application(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Индивидуальное задание (Вариант 8)")
        
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(pady=10, expand=True)
        
        self.create_button_tab()
        self.create_story_tab()
        self.create_checkbox_tab()
        self.create_radiobutton_tab()
        
        self.prime_gen = PrimeGenerator()
        self.fib_gen = FibonacciGenerator()
        self.mersenne_gen = MersennePrimeGenerator()
        self.click_count = 0
        
    def create_button_tab(self):
        self.tab1 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab1, text="Кнопка")
        
        self.button = tk.Button(self.tab1, text="Нажми меня", command=self.on_button_click)
        self.button.pack(pady=20)
        
    def on_button_click(self):
        self.click_count += 1
        option = 2
        
        if option == 1:
            num = self.prime_gen.next_prime()
            text = f"Щелчок {self.click_count}: простое число {num}"
        elif option == 2:
            num = self.fib_gen.next_fibonacci()
            text = f"Щелчок {self.click_count}: число Фибоначчи {num}"
        elif option == 3:
            num = self.mersenne_gen.next_mersenne_prime()
            text = f"Щелчок {self.click_count}: простое Мерсенна {num} (2^{self.mersenne_gen.n}-1)"
        
        self.button.config(text=text)
    
    def create_story_tab(self):
        self.tab2 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab2, text="Рассказ")
        
        self.story_label = tk.Label(self.tab2, text="Начало рассказа:")
        self.story_label.pack(pady=5)
        
        self.story_text = tk.Text(self.tab2, height=5, width=50)
        self.story_text.pack(pady=5)
        self.story_text.insert(tk.END, "Однажды программист решил написать идеальный код. Он работал день и ночь, исправлял баги, оптимизировал алгоритмы...")
        
        self.password_label = tk.Label(self.tab2, text="Введите пароль:")
        self.password_label.pack(pady=5)
        
        self.password_entry = tk.Entry(self.tab2, show="*")
        self.password_entry.pack(pady=5)
        
        self.continue_button = tk.Button(self.tab2, text="Продолжить рассказ", command=self.continue_story)
        self.continue_button.pack(pady=5)
        
        self.ending_label = tk.Label(self.tab2, text="Окончание рассказа:")
        self.ending_label.pack(pady=5)
        
        self.ending_text = tk.Text(self.tab2, height=5, width=50)
        self.ending_text.pack(pady=5)
    
    def continue_story(self):
        password = self.password_entry.get()
        if password == "12345":
            ending = "...и когда наконец все заработало, он понял, что забыл сохранить файл!"
            self.ending_text.delete(1.0, tk.END)
            self.ending_text.insert(tk.END, ending)
        else:
            self.ending_text.delete(1.0, tk.END)
            self.ending_text.insert(tk.END, "Неверный пароль! История останется нераскрытой.")
    
    def create_checkbox_tab(self):
        self.tab3 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab3, text="Флажки")
        
        self.checkbox_label = tk.Label(self.tab3, text="Выберите числа:")
        self.checkbox_label.pack(pady=5)
        
        self.numbers = [1, 2, 4, 8, 16]
        self.check_vars = []
        
        for num in self.numbers:
            var = tk.IntVar()
            cb = tk.Checkbutton(self.tab3, text=str(num), variable=var)
            cb.pack(anchor=tk.W)
            self.check_vars.append(var)
        
        self.calc_button = tk.Button(self.tab3, text="Рассчитать сумму", command=self.calculate_sum)
        self.calc_button.pack(pady=10)
        
        self.result_label = tk.Label(self.tab3, text="Результат:")
        self.result_label.pack(pady=5)
        
        self.result_text = tk.Text(self.tab3, height=2, width=30)
        self.result_text.pack(pady=5)
    
    def calculate_sum(self):
        total = 0
        for i, var in enumerate(self.check_vars):
            if var.get() == 1:
                total += self.numbers[i]
        
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Сумма выбранных чисел: {total}")
    
    def create_radiobutton_tab(self):
        self.tab4 = ttk.Frame(self.notebook)
        self.notebook.add(self.tab4, text="Переключатели")
        
        self.radio_label = tk.Label(self.tab4, text="Выберите тип последовательности:")
        self.radio_label.pack(pady=5)
        
        self.sequence_types = [
            ("Список (list)", "[1, 2, 3]"),
            ("Кортеж (tuple)", "(1, 2, 3)"),
            ("Строка (str)", "'abc'"),
            ("Байты (bytes)", "b'abc'"),
            ("Диапазон (range)", "range(5)")
        ]
        
        self.radio_var = tk.StringVar()
        self.radio_var.set(self.sequence_types[0][1])
        
        for text, value in self.sequence_types:
            rb = tk.Radiobutton(self.tab4, text=text, variable=self.radio_var, value=value)
            rb.pack(anchor=tk.W)
        
        self.radio_result_label = tk.Label(self.tab4, text="Пример литерала:")
        self.radio_result_label.pack(pady=5)
        
        self.radio_result_text = tk.Text(self.tab4, height=2, width=30)
        self.radio_result_text.pack(pady=5)
        
        self.show_button = tk.Button(self.tab4, text="Показать пример", command=self.show_example)
        self.show_button.pack(pady=10)
    
    def show_example(self):
        example = self.radio_var.get()
        self.radio_result_text.delete(1.0, tk.END)
        self.radio_result_text.insert(tk.END, example)

if __name__ == "__main__":
    app = Application()
    app.mainloop()