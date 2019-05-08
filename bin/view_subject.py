from tkinter import Button

# from bin.student import Student

"""
Classe View contenente la parte grafica del programma 
"""


class View_subject(object):

    def __init__(self, master, controller):
        """
        inizializzazione label e bottoni con assegnazione metodi
        :param master:
        """
        self.__window = master
        self.__window.geometry("500x500")
        self.__window.resizable(False, False)
        self.__controller = controller

        self.__math_btn = Button(self.__window, text="MATEMATICA")
        self.__history_btn = Button(self.__window, text="STORIA")
        self.__informatics_btn = Button(self.__window, text="INFORMATICA")

        self.__math_btn.grid(row=1, column=1)
        self.__history_btn.grid(row=2, column=1)
        self.__informatics_btn.grid(row=3, column=1)

# if __name__ == "__main__":
