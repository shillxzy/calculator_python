import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Калькулятор")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.create_widgets()

    def create_widgets(self):
        # Entry для результатів
        result_entry = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="ridge", justify="right")
        result_entry.grid(row=0, column=0, columnspan=4)

        # Кнопки калькулятора
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            'C', '0', '=', '+'
        ]

        row = 1
        col = 0

        for button in buttons:
            tk.Button(self.root, text=button, font=("Arial", 18), width=5, height=2, command=lambda b=button: self.on_button_click(b)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self, button):
        current_text = self.result_var.get()

        if button == 'C':
            self.result_var.set("0")
        elif button == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Помилка")
        else:
            if current_text == "0":
                self.result_var.set(button)
            else:
                self.result_var.set(current_text + button)

if __name__ == "__main__":
    root = tk.Tk()
    calc = Calculator(root)
    root.mainloop()