import pyodbc
from datetime import datetime


class GasStationDataBase:
    def __init__(self, database, server="DESKTOP-31KO856"):
        self.cnxt = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                                   "Server=" + server + ";"
                                                        "Database=" + database + ";"
                                                                                 "Trusted_Connection=yes;")
        self.query = "-- {}\n\n-- Made in Python".format(datetime.now()
                                                         .strftime("%d/%m/%Y"))
        self.cursor = self.cnxt.cursor()

    def select(self):
        cursor = self.cnxt.cursor()
        cursor.execute("SELECT * FROM Client")
        for row in cursor:
            print(row)

        cursor.execute("SELECT * FROM Sale")
        for row in cursor:
            print(row)

    def insert_client(self, args):
        self.cursor.execute("INSERT INTO [Client]\n VALUES\n (%d, \'%s\', \'%s\', \'%s\')" % (int(args[0]), args[1],
                                                                                              args[2], args[3]))
        self.cursor.commit()

    def update_client(self, args):
        self.cursor.execute("UPDATE [Client]\n SET FIO = \'%s\', client_address = \'%s\', client_phone = \'%s\'\n "
                            "WHERE card_account = %d" % (args[1], args[2],
                                                         args[3], int(args[0])))
        self.cursor.commit()

    def delete_client(self, args):
        self.cursor.execute("DELETE [Client]\n WHERE card_account = %d;" % (int(args[0])))
        self.cursor.commit()

    def select_client_info(self):
        s = "Информация о клиентах:\n"
        self.cursor.execute("SELECT * FROM [Client]")
        for row in self.cursor:
            s += "%5d, %50s, %50s, %20s\n" % (row[0], str(row[1]), str(row[2]), str(row[3]))
        return s

    def select_companies_info(self):
        s = "Информация о компаниях:\n"
        self.cursor.execute("SELECT * FROM [Company]")
        for row in self.cursor:
            s += "%5d, %50s, %50s, %20s\n" % (row[0], str(row[1]), str(row[2]), str(row[3]))
        return s

    def insert_company(self, args):
        self.cursor.execute("INSERT INTO [Company]\n VALUES\n (%d, \'%s\', \'%s\', \'%s\')" % (int(args[0]), args[1],
                                                                                               args[2], args[3]))
        self.cursor.commit()

    def update_company(self, args):
        self.cursor.execute("UPDATE [Company]\n SET company_name = \'%s\', company_phone = \'%s\', legal_address = "
                            "\'%s\'\n ""WHERE id_company = %d" % (args[1], args[2],
                                                                  args[3], int(args[0])))
        self.cursor.commit()

    def delete_company(self, args):
        self.cursor.execute("DELETE [Company]\n WHERE id_company = %d;" % (int(args[0])))
        self.cursor.commit()

    def select_fuel_info(self):
        s = "Информация о топливе:\n"
        self.cursor.execute("SELECT * FROM [Fuel]")
        for row in self.cursor:
            # s += "%5d, %20s, %20s, %5s\n" % (row[0], str(row[1]), str(row[2]), row[3])
            s += f"{row[0]:5}, {str(row[1]):20}, {str(row[2]):10}, {row[3]:4}\n"
        return s

    def insert_fuel(self, args):
        self.cursor.execute(
            "INSERT INTO [Fuel]\n VALUES\n (%d, \'%s\', \'%s\', %d)" % (int(args[0]), args[1],
                                                                        args[2], int(args[3])))
        self.cursor.commit()

    def update_fuel(self, args):
        self.cursor.execute("UPDATE [Fuel]\n SET fuel_type = \'%s\', measure_units = \'%s\', price = "
                            "%d\n ""WHERE id_fuel = %d" % (args[1], args[2],
                                                           int(args[3]), int(args[0])))
        self.cursor.commit()

    def delete_fuel(self, args):
        self.cursor.execute("DELETE [Fuel]\n WHERE id_fuel = %d;" % (int(args[0])))
        self.cursor.commit()

    def select_gas_station_info(self):
        s = "Информация о заправках:\n"
        self.cursor.execute("SELECT * FROM [Gas_station]")
        for row in self.cursor:
            s += f"{row[0]:5}, {str(row[1]):20}, {str(row[2]):10}\n"
        return s

    def insert_gas_station(self, args):
        self.cursor.execute(
            "INSERT INTO [Gas_station]\n VALUES\n (%d, \'%s\', %d)" % (int(args[0]), args[1], int(args[2])))
        self.cursor.commit()

    def update_gas_station(self, args):
        self.cursor.execute("UPDATE [Gas_station]\n SET gas_station_address = \'%s\', id_company = %d\n WHERE "
                            "id_gas_station = %d" % (args[1], int(args[2]), int(args[0])))
        self.cursor.commit()

    def delete_gas_station(self, args):
        self.cursor.execute("DELETE [Gas_station]\n WHERE id_gas_station = %d;" % (int(args[0])))
        self.cursor.commit()

    def select_company_fuel_info(self):
        s = "Информация о связи компаний и топлива:\n"
        self.cursor.execute("SELECT * FROM [Company_Fuel]")
        for row in self.cursor:
            s += f"{row[0]:5}, {row[1]:3}\n"
        return s

    def insert_company_fuel(self, args):
        self.cursor.execute(
            "INSERT INTO [Company_Fuel]\n VALUES\n (%d, %d)" % (int(args[0]), int(args[1])))
        self.cursor.commit()

    def delete_company_fuel(self, args):
        self.cursor.execute("DELETE [Company_Fuel]\n WHERE id_company = %d AND id_fuel = %d;" % (int(args[0]),
                                                                                                 int(args[1])))
        self.cursor.commit()

    def select_sale_info(self):
        s = "Информация о продажах:\n"
        self.cursor.execute("SELECT * FROM [Sale]")
        for row in self.cursor:
            s += f"{row[0]:3}, {str(row[1]):20}, {row[2]:6}, {row[3]:6}, {row[4]:6}\n"
        return s

    def insert_sale(self, args):
        self.cursor.execute(
            "INSERT INTO [Sale]\n VALUES\n (%d, \'%s\', %d, %d, %d)" % (int(args[0]), args[1], int(args[2]),
                                                                        int(args[3]), int(args[4])))
        self.cursor.commit()

    def update_sale(self, args):
        self.cursor.execute(f"UPDATE [Sale]\n SET amount = {args[3]}\n WHERE id_fuel = {int(args[0])} "
                                                                        f"AND data = \'{args[1]}\' "
                                                                        f"AND id_gas_station = {int(args[2])} "
                                                                        f"AND card_account = {int(args[4])}")
        self.cursor.commit()

    def delete_sale(self, args):
        self.cursor.execute(f"DELETE [Sale]\n WHERE id_fuel = {int(args[0])} "
                                                    f"AND data = \'{args[1]}\' "
                                                    f"AND id_gas_station = {int(args[2])} "
                                                    f"AND card_account = {int(args[3])}")
        self.cursor.commit()

    def business_get_clients_bills(self):
        s = "Расходы клиентов:\n"
        self.cursor.execute("SELECT [Sale].card_account AS [client], SUM([Sale].amount * [Fuel].price)\nFROM [Sale], "
                            "[Fuel]\nWHERE [Sale].id_fuel = [Fuel].id_fuel\nGROUP BY [Sale].card_account")
        for row in self.cursor:
            s += f"{row[0]:<10} {str(row[1]):>10}\n"
        return s

    def business_get_sale_between_data(self, args):
        s = "Продажи за определённый промежуток времени:\n"
        self.cursor.execute(f"SELECT *\n "
                            f"FROM [Sale]\n "
                            f"WHERE data BETWEEN \'{args[0]}\' AND \'{args[1]}\';")
        for row in self.cursor:
            s += f"{row[0]:3}, {str(row[1]):20}, {row[2]:6}, {row[3]:6}, {row[4]:6}\n"
        return s
