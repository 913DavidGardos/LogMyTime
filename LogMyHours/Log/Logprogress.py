from http import server
from operator import truediv
from zoneinfo import available_timezones


class Log:
    """User Interface for keeping track of daily hours worked"""
    def __init__(self, service):
        self.service = service

    def _cmds(self):
        print("\t[cmds] - shows available commands")
        print("\t[add] [number] - to add to current day the [number] of hours worked")
        print("\t[remove] [date]- to remove today's log")
        print("\t[update] [date] [number] - select any specific date and change the number of hours worked")
        print("\t[print] - print last registered log")
        print("\t[print_all] - print all logs")
        print("\t[exit] - close the program")

    def _request_command_add(self, number):
        self.service.add(number)

    def _request_command_remove(self, date):
        self.service.remove(date)

    def _request_command_update(self, date, value):
        self.service.update(date, value)

    def _request_command_chart(self):
        self.service.print_chart()

    def _request_command_print(self):
        self.service.print_today()

    def _request_command_print_all(self):
        self.service.preatty_print()

    def _request_command_exit(self):
        print("\t_request_command_exit was called")

    def run(self):
        print("\tLog is running...")
        print("\ttype [cmds] for list of available commands\n")

        while(1):
            command = input("<< ")
            array_of_command_args = command.split()

            if command == "exit":
                self.service.save_to_csv()
                break
            
            if command == "cmds":
                self._cmds()

            if array_of_command_args[0] == "add" and len(array_of_command_args) == 2:
                self._request_command_add(array_of_command_args[1])

            if array_of_command_args[0] == "remove" and len(array_of_command_args) == 2:
                self._request_command_remove(array_of_command_args[1])

            if array_of_command_args[0] == "update" and len(array_of_command_args) == 3:
                self._request_command_update(array_of_command_args[1], array_of_command_args[2])

            if command == "chart":
                self._request_command_chart()

            if command == "print":
                self._request_command_print()

            if command == "print_all":
                self._request_command_print_all()