from tkinter import messagebox
from GasStationDataBase import *


class Window:
    def __init__(self, window, __client_tab, __company_tab, __fuel_tab, __gas_station_tab, __company_fuel_tab,
                 __sale_tab, __business_tab):
        __client_tab.add_window(self)
        __company_tab.add_window(self)
        __fuel_tab.add_window(self)
        __gas_station_tab.add_window(self)
        __company_fuel_tab.add_window(self)
        __sale_tab.add_window(self)
        __business_tab.add_window(self)

        self.__gas_station_data_base = GasStationDataBase("gas_station")
        __client_tab.print_info()
        __company_tab.print_info()
        __fuel_tab.print_info()
        __gas_station_tab.print_info()
        __company_fuel_tab.print_info()
        __sale_tab.print_info()

    def notify(self, sender, event, *args):
        if sender == "ClientTab":
            if event == "INSERT":
                try:
                    int(args[0])
                    if len(args[0]) == 5 and len(args[1]) > 0 and len(args[2]) > 0 and len(args[3]) > 0:
                        self.__gas_station_data_base.insert_client(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
            if event == "get_info":
                print()
                return self.__gas_station_data_base.select_client_info()
            if event == "DELETE":
                try:
                    int(args[0])
                    if len(args[0]) == 5:
                        self.__gas_station_data_base.delete_client(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
            if event == "UPDATE":
                try:
                    int(args[0])
                    if len(args[0]) == 5 and len(args[1]) > 0 and len(args[2]) > 0 and len(args[3]) > 0:
                        self.__gas_station_data_base.update_client(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
        elif sender == "CompanyTab":
            if event == "INSERT":
                try:
                    int(args[0])
                    if len(args[0]) == 4 and len(args[1]) > 0 and len(args[2]) > 0 and len(args[3]) > 0:
                        self.__gas_station_data_base.insert_company(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
            if event == "get_info":
                return self.__gas_station_data_base.select_companies_info()
            if event == "DELETE":
                try:
                    int(args[0])
                    if len(args[0]) == 4:
                        self.__gas_station_data_base.delete_company(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
            if event == "UPDATE":
                try:
                    int(args[0])
                    if len(args[0]) == 4 and len(args[1]) > 0 and len(args[2]) > 0 and len(args[3]) > 0:
                        self.__gas_station_data_base.update_company(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
        elif sender == "FuelTab":
            if event == "INSERT":
                try:
                    int(args[0])
                    if len(args[0]) == 1 and len(args[1]) > 0 and len(args[2]) > 0 and int(args[3]) > 0:
                        self.__gas_station_data_base.insert_fuel(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
            if event == "get_info":
                return self.__gas_station_data_base.select_fuel_info()
            if event == "DELETE":
                try:
                    int(args[0])
                    if len(args[0]) == 1:
                        self.__gas_station_data_base.delete_fuel(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
            if event == "UPDATE":
                try:
                    int(args[0])
                    if len(args[0]) == 1 and len(args[1]) > 0 and len(args[2]) > 0 and int(args[3]) > 0:
                        self.__gas_station_data_base.update_fuel(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
        elif sender == "GasStationTab":
            if event == "INSERT":
                try:
                    int(args[0]), int(args[2])
                    if len(args[0]) == 5 and len(args[1]) > 0 and len(args[2]) == 4:
                        self.__gas_station_data_base.insert_gas_station(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
            if event == "get_info":
                return self.__gas_station_data_base.select_gas_station_info()
            if event == "DELETE":
                try:
                    int(args[0])
                    if len(args[0]) == 5:
                        self.__gas_station_data_base.delete_gas_station(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
            if event == "UPDATE":
                try:
                    int(args[0]), int(args[2])
                    if len(args[0]) == 5 and len(args[1]) > 0 and len(args[2]) == 4:
                        self.__gas_station_data_base.update_gas_station(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
        elif sender == "CompanyFuelTab":
            if event == "INSERT":
                try:
                    int(args[0]), int(args[1])
                    if len(args[0]) == 4 and len(args[1]) == 1:
                        self.__gas_station_data_base.insert_company_fuel(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
            if event == "get_info":
                return self.__gas_station_data_base.select_company_fuel_info()
            if event == "DELETE":
                try:
                    int(args[0]), int(args[1])
                    if len(args[0]) == 4 and len(args[1]) == 1:
                        self.__gas_station_data_base.delete_company_fuel(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
        elif sender == "SaleTab":
            if event == "INSERT":
                try:
                    int(args[0]), int(args[2]), int(args[3]), int(args[4])
                    if len(args[0]) == 1 and len(args[1]) > 0 and len(args[2]) == 5 and int(args[3]) > 0 and \
                            len(args[4]) == 5:
                        self.__gas_station_data_base.insert_sale(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
            if event == "get_info":
                return self.__gas_station_data_base.select_sale_info()
            if event == "DELETE":
                try:
                    int(args[0]), int(args[2]), int(args[3])
                    if len(args[0]) == 1 and len(args[1]) > 0 and len(args[2]) == 5 and len(args[3]) == 5:
                        self.__gas_station_data_base.delete_sale(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
            if event == "UPDATE":
                try:
                    int(args[0]), int(args[2]), int(args[3]), int(args[4])
                    if len(args[0]) == 1 and len(args[1]) > 0 and len(args[2]) == 5 and int(args[3]) > 0 and \
                            len(args[4]) == 5:
                        self.__gas_station_data_base.update_sale(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
        elif sender == "BusinessTab":
            if event == "Посчитать затраты клиентов":
                return self.__gas_station_data_base.business_get_clients_bills()
            elif event == "Продажи за промежуток времени":
                try:
                    return self.__gas_station_data_base.business_get_sale_between_data(args)
                except Exception:
                    messagebox.showerror("Ошибка", "Передан неверный аргумент")
