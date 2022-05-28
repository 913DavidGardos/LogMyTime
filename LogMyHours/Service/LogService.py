
class Service:
    """Service is going to manage the commands from log""" 
    def __init__(self, db):
        self._db = db

    def add(self, number):
        self._db.add(number)

    def preatty_print(self):
        self._db.preatty_print()

    def update(self, date, value):
        self._db.update(date, value)
    
    def save_to_csv(self):
        self._db.closing_db()

    def remove(self, date):
        self._db.remove(date)

    def print_today(self):
        self._db.print_today()

    def print_chart(self):
        self._db.print_chart()