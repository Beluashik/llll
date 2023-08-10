import tkinter

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("calculator")

        self.result_var = tkinter.StringVar() # Переменная для хранения результатов вычисления

        self.entry = tkinter.Entry(self.root, textvariable=self.result_var, font=('Ariel', 16))
        self.entry.grid(row=0, column=0, columnspan=4)

        self.buttons = [
            ('1', 1, 0),
            ('2', 1, 1),
            ('3', 1, 2),
            ('4', 2, 0),
            ('5', 2, 1),
            ('6', 2, 2),
            ('7', 3, 0),
            ('8', 3, 1),
            ('9', 3, 2),
            ('0', 4, 0),
            ('.', 4, 1),
            ('=', 4, 2),
            ('+', 3, 3),
            ('-', 4, 3),
            ('*', 2, 3),
            ('/', 1, 3),
        ]

        for (text, row, column) in self.buttons:
            button = tkinter.Button(self.root, text=text, font=('Ariel', 16), command=lambda t=text: self._button_click(t))
            button.grid(row=row, column=column, padx=10, pady=10, sticky='nsew')

    def _button_click(self, text):
        '''
        обработка нажатия на кнопку
        :param text: значение
        :return:
        '''
        if text == '=':
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception:
                self.result_var.set('Ошибка')
        else:
            current_text = self.result_var.get()
            self.result_var.set(current_text + text)



if __name__ == '__main__':
    root = tkinter.Tk()
    app = CalculatorApp(root)
    root.mainloop()