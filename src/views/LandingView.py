from views.lib.Menu import Menu
from .RetrieveDataView import RetrieveDataView
from .DebugView import DebugView

class LandingView:
    def __init__(self):
        pass

    def render(self):
        options = ["Add data", "Retrieve data", "Debug", "Quit"]
        menu = Menu(options)
        selection = menu.render()
        if (selection == 0):
            print(0)
        elif (selection == 1):
            retrieveDataView = RetrieveDataView()
            retrieveDataView.render()
        elif (selection == 2):
            debugView = DebugView()
            debugView.render()
        elif (selection ==3 ):
            return 0  # Exit render loop

        self.render()
