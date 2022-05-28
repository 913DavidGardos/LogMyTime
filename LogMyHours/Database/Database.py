from datetime import date
from File.File import File

class Database:
    """Database is going to store everything into a file for now"""
    def __init__(self):
        self._map_of_logs = []
        self._myfile = File('read')
        self._populate_list()
        self._myfile.close()

    def _populate_list(self):
        for row in self._myfile.get_file_var():
            self._map_of_logs.append({'Date':row['Date'],'Hours':row['Hours']})

    def preatty_print(self):
        for item in self._map_of_logs:
            print(item['Date'], item['Hours'])

    def add(self, number):
        mystring = self._nr_to_X_string(number)
                
        for dict_item in self._map_of_logs:
            if(dict_item["Date"] == str(date.today())):
                return

        self._map_of_logs.append({"Date": str(date.today()), "Hours": mystring})  

    def _nr_to_X_string(self, nr):
        mystring = ""
        for i in range(int(nr)):
            mystring += "X "

        return mystring

    def update(self, date, value):
        dict_to_be_changed = self._find_by_date(date)
        
        if(dict_to_be_changed == 0):
            print("\tException: there is no item in the database with that description!")
            return
        
        dict_to_be_changed["Hours"] = self._nr_to_X_string(value)

    def _find_by_date(self, date):
        for i in self._map_of_logs:
            if(i["Date"] == date):
                return i

        return 0

    def remove(self, date):
        item = self._find_by_date(date)
        if(item == 0):
            print("\tException: there is no item in the database with that description!")

        self._map_of_logs.remove(item)

    def print_today(self):
        size = len(self._map_of_logs)
        print(self._map_of_logs[size - 1]['Date'], self._map_of_logs[size - 1]['Hours'])
    
    def closing_db(self):
        self._myfile = File('write')
        self._myfile.get_file_var().writerows(self._map_of_logs)
        self._myfile.close()

    