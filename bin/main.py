# --IMPORT
import time

from bin.controller import Controller

# --VARIABLES

boolD = True

# --FUNCTIONS

# --MAIN

if __name__ == "__main__":
    if boolD:
        print("Started")

    controller = Controller()
    controller.run()


    if boolD:
        print("Ended")
