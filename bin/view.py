from tkinter import Button, Entry, Label
from bin.teacher import Teacher
from bin.student import Student


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

        self.__model_teacher = Teacher()
        self.__model_student = Student()
        self.__controller = Controller()

        self.__window.columnconfigure(1, weight=1)
        self.__window.columnconfigure(5, weight=1)
        self.__window.rowconfigure(1, weight=1)
        self.__window.rowconfigure(7, weight=1)
        self.__window.columnconfigure(3, weight=1)
        # self.__window.columnconfigure(3, weight=4)

        self.__label_title = Label(self.__window, text="LEZIONI TRA PARI")
        self.__label_title.grid(row=1, column=2, columnspan=3)

        self.__label_name = Label(self.__window, text="First Name   ")
        self.__label_name.grid(row=2, column=2, columnspan=3)

        self.__Entry_name = Entry(self.__window)
        self.__Entry_name.grid(row=3, column=2, columnspan=3)

        self.__label_surname = Label(self.__window, text="Last Name   ")
        self.__label_surname.grid(row=4, column=2, columnspan=3)

        self.__Entry_surname = Entry(self.__window)
        self.__Entry_surname.grid(row=5, column=2, columnspan=3)

        self.__window.rowconfigure(6, weight=0)

        self.__teacher_button = Button(self.__window, text="Teacher")
        self.__student_button = Button(self.__window, text="Student")

        self.__teacher_button.grid(row=7, column=2)
        self.__student_button.grid(row=7, column=4)

# if __name__ == "__main__":
