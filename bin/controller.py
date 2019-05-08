# from bin.view import View
import tkinter as tk

"""
classe controller per esecuzione grafica 2
"""


class Controller(object):
    def __init__(self, view):
        self.__root = tk.Tk()
        self.__view = view(self.__root, self)

    def run(self):
        self.__root.title("Lezioni tra pari")
        self.__root.mainloop()

    def stop(self):
        self.__root.destroy()


if __name__ == '__main__':
    c = Controller()
    c.run()
