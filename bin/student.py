from bin.controller import Controller
from bin.user import User
from bin.view_subject import View_subject


class Student(User):
    def __init__(self):
        User.__init__(self)
        self.__class = None
        self.__id_student = None

    def viewSubject(self, entry_first_name, entry_last_name, controller):
        self.set_first_name(entry_first_name.get())
        self.set_last_name(entry_last_name.get())

        "stop della finestra di login"
        controller.stop()

        "istanza un nuovo controller per aprire una nuova finestra"
        controller_view_subject = Controller(View_subject)
        controller_view_subject.run()


    def doQuiz(self):
        return

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name


if __name__ == "__main__":
    a = Student()
    print(a.__dict__)




