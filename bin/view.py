from tkinter import Button, Entry, Label

"""
Classe View contenente la parte grafica del programma 
"""


class View(object):

    def __init__(self, master):
        """
        inizializzazione label e bottoni con assegnazione metodi
        :param master:
        """
        self.__window = master
        self.__window.geometry("500x500")
        self.__window.resizable(False, False)
        # self.__model = Mossa_grafica()

        self.__window.columnconfigure(1, weight=1)
        self.__window.columnconfigure(5, weight=1)
        self.__window.rowconfigure(1, weight=1)
        self.__window.rowconfigure(7, weight=1)

        self.__labelname = Label(self.__window, text="First Name   ")
        self.__labelname.grid(row=2, column=2, columnspan=3)

        self.__Entryname = Entry(self.__window)
        self.__Entryname.grid(row=3, column=2, columnspan=3)

        self.__labelsurname = Label(self.__window, text="Last Name   ")
        self.__labelsurname.grid(row=4, column=2, columnspan=3)

        self.__Entrysurname = Entry(self.__window)
        self.__Entrysurname.grid(row=5, column=2, columnspan=3)

        self.__window.rowconfigure(6, weight=0)

        self.__teacher_button = Button(self.__window, text="teacher")
        self.__student_button = Button(self.__window, text="student")

        # self.__window.columnconfigure(3, weight=4)
        self.__window.columnconfigure(3, weight=1)
        self.__teacher_button.grid(row=7, column=2)
        self.__student_button.grid(row=7, column=4)
