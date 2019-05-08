# --IMPORT

from bin.controller import Controller
from bin.view_login import View

# --VARIABLES

boolD = True

# --FUNCTIONS

# --MAIN

if __name__ == "__main__":
    if boolD:
        print("Started")

    controller = Controller(View)
    controller.run()


    if boolD:
        print("Ended")
