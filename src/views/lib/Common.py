SCREEN_WIDTH = 40  # characters


def pause():
    showPrompt("Press enter to continue")


def showPrompt(prompt):
    return input("\n{0}:".format(prompt))


def showBreak():
    rowBreak = ""
    for i in range(SCREEN_WIDTH):
        rowBreak += "-"
    print(rowBreak)


def clearScreen():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    showBreak()
