from .Common import clearScreen, showPrompt

class Menu:
    def __init__(self, options):
        self.options = options

    def render(self):
        clearScreen()
        for idx, option in enumerate(self.options):
            print("{0}. {1}".format(idx, option))
        res = showPrompt("Select option by index")
        return int(res)