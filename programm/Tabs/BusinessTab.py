from tkinter import *
from tkinter.ttk import *


class BusinessTab(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        frame1 = Frame(self)
        frame1.pack(fill=X)
        execute_button = Button(frame1, text="Выполнить", command=self.__click_button_fill)
        execute_button.pack(side=RIGHT, padx=5)

        self.combo_modify_data = Combobox(frame1, width=50)
        self.combo_modify_data["values"] = ('Выберите команду', "Посчитать затраты клиентов",
                                            "Продажи за промежуток времени")
        self.combo_modify_data.current(0)
        self.combo_modify_data.bind("<<ComboboxSelected>>", self.__change_insert_method)
        self.combo_modify_data.pack(side=LEFT, padx=5, pady=5)

        frame2 = Frame(self)
        frame2.pack(fill=X)
        self.label_data_start = Label(frame2, text="Введите начальную дату(ГГГГ-ДД-ММ ЧЧ:ММ:СС)", width=50)
        self.label_data_start.pack(side=LEFT, pady=5)
        self.entry_data_start = Entry(frame2)
        self.entry_data_start.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)
        self.label_data_end = Label(frame3, text="Введите конечную дату(ГГГГ-ДД-ММ ЧЧ:ММ:СС)", width=50)
        self.label_data_end.pack(side=LEFT, pady=5)
        self.entry_data_end = Entry(frame3)
        self.entry_data_end.pack(fill=X, padx=5, expand=True)

        self.label_fuel_info = Label(self, font=12)
        self.label_fuel_info.pack(fill=BOTH)

        self.__hide_elements()

    def add_window(self, window):
        self.__window = window

    def __hide_elements(self):
        self.label_data_start.pack_forget()
        self.entry_data_start.pack_forget()
        self.label_data_end.pack_forget()
        self.entry_data_end.pack_forget()

    def __change_insert_method(self, event):
        if self.combo_modify_data.get() in ["Выберите команду", "Посчитать затраты клиентов"]:
            self.__hide_elements()
        elif self.combo_modify_data.get() == "Продажи за промежуток времени":
            self.__hide_elements()
            self.label_data_start.pack(side=LEFT, pady=5)
            self.entry_data_start.pack(fill=X, padx=5, expand=True)
            self.label_data_end.pack(side=LEFT, pady=5)
            self.entry_data_end.pack(fill=X, padx=5, expand=True)

    def __click_button_fill(self):
        s = ""
        if self.combo_modify_data.get() == "Посчитать затраты клиентов":
            s = self.__window.notify(self.__class__.__name__, self.combo_modify_data.get())
        elif self.combo_modify_data.get() == "Продажи за промежуток времени":
            s = self.__window.notify(self.__class__.__name__, self.combo_modify_data.get(),
                                     self.entry_data_start.get(),
                                     self.entry_data_end.get())
        self.label_fuel_info.configure(text=s)
