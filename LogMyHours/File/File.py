import csv

class File:
    def __init__(self, option):
        self._option = option
        self._filename = "Loggata.csv"
        if(self._option == 'read'):
            self._csvfile = open(self._filename, newline='')
            self._c = csv.DictReader(self._csvfile)
        elif(self._option == 'write'):
            self._csvfile = open(self._filename, 'w')
            self._headers = ["Date", "Hours"]
            self._c = csv.DictWriter(self._csvfile, fieldnames=self._headers)
            self._c.writeheader()
        else:
            print("Error in File initiator")

    def get_file_var(self):
        return self._c

    def close(self):
        self._csvfile.close()
