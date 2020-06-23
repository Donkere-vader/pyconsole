""" Fore more information visit: https://ozzmaker.com/add-colour-to-text-in-python/ """

class Colors:
    def __init__(self):
        self._colors_dict = {  # for bg + 10
            "black": 30,
            "red": 31,
            "green": 32,
            "yellow": 33,
            "blue": 34,
            "purple": 35,
            "cyan": 36,
            "white": 37
        }
        self._font_weight_dict = {
            "bold": 1,
            "underline": 2,
            "negative": 3,
            "negative2": 5 
        }

    def reset_color(self):
        """ Reset the color of the terminal output """
        print("\033[0;37;40m", end="")

    def set_color(self, fg='white', bg='black', fw=None):
        """ Set the color of the terminal output """
        _fg = self._colors_dict[fg.lower()]
        _bg = self._colors_dict[bg.lower()] + 10

        _fw = 0
        if fw:
            _fw = self._font_weight_dict[fw.lower()]

        print(f"\033[{_fw};{_fg};{_bg}m",end="")