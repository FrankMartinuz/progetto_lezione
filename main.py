# --IMPORT

from tkinter import *

# --VARIABLES

boolD = True

# --FUNCTIONS

# --MAIN

if __name__ == "__main__":
    if boolD:
        print("Started")

        root = Tk()
        root.geometry("500x500")
        root.resizable(False, False)

        root.columnconfigure(1, weight=1)
        root.columnconfigure(5, weight=1)
        root.rowconfigure(1, weight=1)
        root.rowconfigure(6, weight=1)

        label = Label(root, text="Prova")
        label.grid(row=2, column=2, columnspan=3)

        root.rowconfigure(3, weight=1)

        teacher_button = Button(root, text="teacher")
        student_button = Button(root, text="student")

        # root.columnconfigure(2, weight=4)
        root.columnconfigure(3, weight=1)
        teacher_button.grid(row=4, column=2)
        student_button.grid(row=4, column=4)

        root.mainloop()

    if boolD:
        print("Ended")
