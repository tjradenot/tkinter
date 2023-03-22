import tkinter as tk
import ttkbootstrap as ttk

TITLE = 'Miles to km'
SIZE = '300x150'


class Application:

    def __init__(self, title, size):
        self.window = ttk.Window(themename='journal')
        self.window.title(title)
        self.window.geometry(size)

        self.km_output = 0

        # title
        self.title_label = tk.Label(
            self.window, text=title, font='Calibri 24 bold')
        self.title_label.pack()

        # input field
        self.input_frame = ttk.Frame(self.window)

        # специальный объект ткинтера, который позволяет хранить и обновлять целочисленное значение
        self.entry_int = tk.IntVar()

        # textvariable - коннектим self.entryInt к self.entry.
        # Все что будет введено в self.entry будет завписываться в self.entryint
        self.entry = ttk.Entry(
            self.input_frame,
            textvariable=self.entry_int)

        self.button = ttk.Button(
            self.input_frame, text='Convert', command=self.convert)
        self.entry.pack(side='left', padx=5)
        self.button.pack(side='left')
        self.input_frame.pack()

        # output
        self.output_string = tk.StringVar()
        self.output = ttk.Label(
            self.window,
            text='Output',
            font='Calibri 24',
            textvariable=self.output_string)
        self.output.pack(pady=5)

        # bind Enter key
        self.window.bind('<Return>', self.enter_key)

        # run
        self.window.mainloop()

    def enter_key(self, event):
        """Вызывает фугкцию convert при нажатии на Enter"""
        self.convert()

    def convert(self):
        self.km_output = self.entry_int.get() * 1.61
        self.output_string.set(self.km_output)


if __name__ == '__main__':

    app = Application(TITLE, SIZE)
