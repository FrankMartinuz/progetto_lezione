from bin.user import Lesson
from bin.user import User


class Teacher(User):
    def __init__(self):
        User.__init__(self)
        self.__subject = None
        self.__id_teacher = str(self._first_name + self._last_name)

    def chooseSubject(self, subject):
        self.__subject = subject

    def addLesson(self, idt, title, desc, text, link):
        lesson = Lesson(idt, title, desc, text, link)
        lesson.createLesson()

    def removeLesson(self):
        return

    def addQuiz(self):
        quiz = Quiz()
        quiz.createQuiz()
        return

    def removeQuiz(self):
        return


if __name__ == "__main__":
    a = Teacher()
    print(a.__dict__)
