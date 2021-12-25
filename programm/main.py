from Window import *
from tkinter import ttk
from tkinter import *
from Tabs import ClientTab
from Tabs import CompanyTab
from Tabs import FuelTab
from Tabs import GasStationTab
from Tabs import CompanyFuelTab
from Tabs import SaleTab
from Tabs import BusinessTab

if __name__ == '__main__':
    window = Tk()
    window.geometry('1200x800')
    tab_control = ttk.Notebook(window)
    client_tab = ClientTab.ClientTab()
    company_tab = CompanyTab.CompanyTab()
    fuel_tab = FuelTab.FuelTab()
    gas_station_tab = GasStationTab.GasStationTab()
    company_fuel_tab = CompanyFuelTab.CompanyFuelTab()
    sale_tab = SaleTab.SaleTab()
    business_tab = BusinessTab.BusinessTab()

    tab_control.add(client_tab, text="Client")
    tab_control.add(company_tab, text="Company")
    tab_control.add(fuel_tab, text="Fuel")
    tab_control.add(gas_station_tab, text="Gas station")
    tab_control.add(company_fuel_tab, text="Company fuel")
    tab_control.add(sale_tab, text="Sale")
    tab_control.add(business_tab, text="Бизнес методы")
    tab_control.pack(expand=1, fill='both')
    window_t = Window(window, client_tab, company_tab, fuel_tab, gas_station_tab, company_fuel_tab, sale_tab,
                      business_tab)
    window.mainloop()
