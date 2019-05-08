from bin.controller import Controller
from bin.lesson import Lesson
from bin.user import User
from bin.view_subject import View_subject


class Teacher(User):
    def __init__(self):
        User.__init__(self)
        self.__subject = None
        self.__id_teacher = None

    def viewSubject(self, entry_first_name, entry_last_name, controller):
        self.set_first_name(entry_first_name.get())
        self.set_last_name(entry_last_name.get())

        "stop della finestra di login"
        controller.stop()

        "istanza un nuovo controller per aprire una nuova finestra"
        controller_view_subject = Controller(View_subject)
        controller_view_subject.run()

    def addLesson(self, idt, title, desc, text, link):
        lesson = Lesson(idt, title, desc, text, link)
        lesson.createLesson()

    def removeLesson(self):
        return

    # def addQuiz(self):
    #     quiz = Quiz()
    #     quiz.createQuiz()
    #     return

    def removeQuiz(self):
        return

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name


if __name__ == "__main__":
    a = Teacher()
    print(a.__dict__)
