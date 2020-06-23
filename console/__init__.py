from colors import Colors
from table import Table
from pyfiglet import Figlet
import datetime
import platform
import os

class Console:
    def __init__(self, program_name=None, log=True, pin=None, log_display_length=10):
        self.colors = Colors()
        self.program_name = program_name
        self.do_log = log
        self.log_dir = './logs'
        self.pin = pin
        self.log_display_length = log_display_length
        self.logs = []  # the log
    
        self.figlet = Figlet(font='ANSI_shadow')
        
        # define the clear screen function
        if platform.system() == "Windows":
            self.clear_screen = lambda cmnd="cls": os.system(cmnd)
        else:
            self.clear_screen = lambda cmnd="clear": os.system(cmnd)

        self.start()

    def start(self):
        try:
            self.log_file = open(f"{self.log_dir}/{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')}", "a")
        except FileNotFoundError:
            os.mkdir(self.log_dir)
            self.log_file = open(f"{self.log_dir}/{datetime.datetime.now().strftime('%Y_%m_%d_%H_%M')}", "a")

        self.output()


    def print_logo(self):
        self.colors.set_color(fg='red')
        print(self.figlet.renderText(self.program_name))
        self.colors.reset_color()

    def output(self):
        self.clear_screen()
        if self.program_name:
            self.print_logo()
        print()
        if self.pin:
            print(self.pin)

        self.colors.set_color(fg='green')
        print()
        print('[===========] LOGS [===========]')
        self.colors.reset_color()
        for log_item in self.logs[:10]:
            self.colors.set_color(fg='black', bg='green')
            print(log_item['timestamp'], end="")
            self.colors.reset_color()
            print("", log_item['data'])

    def log(self, data):
        _log_item = {
            "timestamp": f"[{datetime.datetime.now().strftime('%Y/%M/%d %H:%M')}]",
            "data": data
        }
        self.logs.append(_log_item)
        self.output()

        self.log_file.write(f"{_log_item['timestamp']} {_log_item['data']}")