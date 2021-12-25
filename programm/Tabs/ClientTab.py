from tkinter import *
from tkinter.ttk import *


class ClientTab(Frame):
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
        self.label_card_account = Label(frame2, text="Введите номер карт-счёта клиента", width=40)
        self.label_card_account.pack(side=LEFT, pady=5)
        self.entry_card_account = Entry(frame2)
        self.entry_card_account.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)
        self.label_fio = Label(frame3, text="Введите ФИО клиента", width=40)
        self.label_fio.pack(side=LEFT, pady=5)
        self.entry_fio = Entry(frame3)
        self.entry_fio.pack(fill=X, padx=5, expand=True)

        frame4 = Frame(self)
        frame4.pack(fill=X)
        self.label_address = Label(frame4, text="Введите адресс клиента", width=40)
        self.label_address.pack(side=LEFT, pady=5)
        self.entry_address = Entry(frame4)
        self.entry_address.pack(fill=X, padx=5, expand=True)

        frame5 = Frame(self)
        frame5.pack(fill=X)
        self.label_phone_number = Label(frame5, text="Введите телефон клиента", width=40)
        self.label_phone_number.pack(side=LEFT, pady=5)
        self.entry_phone_number = Entry(frame5)
        self.entry_phone_number.pack(fill=X, padx=5, expand=True)

        self.label_clients_info = Label(self, font=12)
        self.label_clients_info.pack(fill=BOTH)

        self.__hide_elements()

    def add_window(self, window):
        self.__window = window

    def __hide_elements(self):
        self.label_card_account.pack_forget()
        self.entry_card_account.pack_forget()
        self.label_fio.pack_forget()
        self.entry_fio.pack_forget()
        self.label_address.pack_forget()
        self.entry_address.pack_forget()
        self.label_phone_number.pack_forget()
        self.entry_phone_number.pack_forget()

    def __click_button_fill(self):
        if self.combo_modify_data.get() in ["INSERT", "UPDATE"]:
            self.__window.notify(self.__class__.__name__, self.combo_modify_data.get(),
                                 self.entry_card_account.get(),
                                 self.entry_fio.get(),
                                 self.entry_address.get(),
                                 self.entry_phone_number.get())
        elif self.combo_modify_data.get() == "DELETE":
            self.__window.notify(self.__class__.__name__, self.combo_modify_data.get(),
                                 self.entry_card_account.get())
        self.print_info()

    def __change_insert_method(self, event):
        if self.combo_modify_data.get() == "Выберите команду":
            self.__hide_elements()
        elif self.combo_modify_data.get() == "DELETE":
            self.__hide_elements()
            self.label_card_account.pack(side=LEFT, pady=5)
            self.entry_card_account.pack(fill=X, padx=5, expand=True)
        else:
            self.label_card_account.pack(side=LEFT, pady=5)
            self.entry_card_account.pack(fill=X, padx=5, expand=True)
            self.label_fio.pack(side=LEFT, pady=5)
            self.entry_fio.pack(fill=X, padx=5, expand=True)
            self.label_address.pack(side=LEFT, pady=5)
            self.entry_address.pack(fill=X, padx=5)
            self.label_phone_number.pack(side=LEFT, pady=5)
            self.entry_phone_number.pack(fill=X, padx=5)

    def print_info(self):
        s = self.__window.notify(self.__class__.__name__, "get_info")
        self.label_clients_info.configure(text=s)
