from tkinter import *
from tkinter.ttk import *


class SaleTab(Frame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        frame1 = Frame(self)
        frame1.pack(fill=X)
        execute_button = Button(frame1, text="Выполнить", command=self.__click_button_fill)
        execute_button.pack(side=RIGHT, padx=5)

        self.combo_modify_data = Combobox(frame1, width=20)
        self.combo_modify_data["values"] = ('Выберите команду', "INSERT", "UPDATE", "DELETE")
        self.combo_modify_data.current(0)
        self.combo_modify_data.bind("<<ComboboxSelected>>", self.__change_insert_method)
        self.combo_modify_data.pack(side=LEFT, padx=5, pady=5)

        frame2 = Frame(self)
        frame2.pack(fill=X)
        self.label_id_fuel = Label(frame2, text="Введите id топлива", width=40)
        self.label_id_fuel.pack(side=LEFT, pady=5)
        self.entry_id_fuel = Entry(frame2)
        self.entry_id_fuel.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)
        self.label_data = Label(frame3, text="Введите дату(ГГГГ-ДД-ММ ЧЧ:ММ:СС)", width=40)
        self.label_data.pack(side=LEFT, pady=5)
        self.entry_data = Entry(frame3)
        self.entry_data.pack(fill=X, padx=5, expand=True)

        frame4 = Frame(self)
        frame4.pack(fill=X)
        self.label_id_gas_station = Label(frame4, text="Введите id заправки", width=40)
        self.label_id_gas_station.pack(side=LEFT, pady=5)
        self.entry_id_gas_station = Entry(frame4)
        self.entry_id_gas_station.pack(fill=X, padx=5, expand=True)

        frame5 = Frame(self)
        frame5.pack(fill=X)
        self.label_amount = Label(frame5, text="Введите количество топлива", width=40)
        self.label_amount.pack(side=LEFT, pady=5)
        self.entry_amount = Entry(frame5)
        self.entry_amount.pack(fill=X, padx=5, expand=True)

        frame6 = Frame(self)
        frame6.pack(fill=X)
        self.label_card_account = Label(frame6, text="Введите номер карт-счёта клиента", width=40)
        self.label_card_account.pack(side=LEFT, pady=5)
        self.entry_card_account = Entry(frame6)
        self.entry_card_account.pack(fill=X, padx=5, expand=True)

        self.label_companies_info = Label(self, font=12)
        self.label_companies_info.pack(fill=BOTH)

        self.__hide_elements()

    def add_window(self, window):
        self.__window = window

    def __hide_elements(self):
        self.label_id_fuel.pack_forget()
        self.entry_id_fuel.pack_forget()
        self.label_data.pack_forget()
        self.entry_data.pack_forget()
        self.label_id_gas_station.pack_forget()
        self.entry_id_gas_station.pack_forget()
        self.label_amount.pack_forget()
        self.entry_amount.pack_forget()
        self.label_card_account.pack_forget()
        self.entry_card_account.pack_forget()

    def __click_button_fill(self):
        if self.combo_modify_data.get() in ["INSERT", "UPDATE"]:
            self.__window.notify(self.__class__.__name__, self.combo_modify_data.get(),
                                 self.entry_id_fuel.get(),
                                 self.entry_data.get(),
                                 self.entry_id_gas_station.get(),
                                 self.entry_amount.get(),
                                 self.entry_card_account.get())
        elif self.combo_modify_data.get() == "DELETE":
            self.__window.notify(self.__class__.__name__, self.combo_modify_data.get(),
                                 self.entry_id_fuel.get(),
                                 self.entry_data.get(),
                                 self.entry_id_gas_station.get(),
                                 self.entry_card_account.get())
        self.print_info()

    def __change_insert_method(self, event):
        if self.combo_modify_data.get() == "Выберите команду":
            self.__hide_elements()
        elif self.combo_modify_data.get() == "DELETE":
            self.__hide_elements()
            self.label_id_fuel.pack(side=LEFT, pady=5)
            self.entry_id_fuel.pack(fill=X, padx=5, expand=True)
            self.label_data.pack(side=LEFT, pady=5)
            self.entry_data.pack(fill=X, padx=5, expand=True)
            self.label_id_gas_station.pack(side=LEFT, pady=5)
            self.entry_id_gas_station.pack(fill=X, padx=5, expand=True)
            self.label_card_account.pack(side=LEFT, pady=5)
            self.entry_card_account.pack(fill=X, padx=5, expand=True)
        else:
            self.label_id_fuel.pack(side=LEFT, pady=5)
            self.entry_id_fuel.pack(fill=X, padx=5, expand=True)
            self.label_data.pack(side=LEFT, pady=5)
            self.entry_data.pack(fill=X, padx=5, expand=True)
            self.label_id_gas_station.pack(side=LEFT, pady=5)
            self.entry_id_gas_station.pack(fill=X, padx=5, expand=True)
            self.label_amount.pack(side=LEFT, pady=5)
            self.entry_amount.pack(fill=X, padx=5, expand=True)
            self.label_card_account.pack(side=LEFT, pady=5)
            self.entry_card_account.pack(fill=X, padx=5, expand=True)

    def print_info(self):
        self.label_companies_info.configure(text=self.__window.notify(self.__class__.__name__, "get_info"))
