from views.lib.Menu import Menu


class RetrieveDataView:
    def __init__(self):
        pass

    def render(self):
        options = ["Get all users", "Get all doctors", "Get all Visits", "Back"]
        menu = Menu(options)
        selection = menu.render()
        if (selection == 0):
            print(0)
        elif (selection == 1):
            print(1)
        elif (selection == 2):
            print(1)
        elif (selection == 3):
            pass  # Allow render to complete
        else:
            self.render()
