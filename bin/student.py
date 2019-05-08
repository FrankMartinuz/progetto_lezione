from config.user import User


class Student(User):
    def __init__(self):
        User.__init__(self)
        self.__class = None
        self.__id_student = str(self._first_name + self._last_name)

    def chooseSubject(self, subject):
        self.__subject = subject

    def doQuiz(self):
        return


if __name__ == "__main__":
    a = Student()
    print(a.__dict__)
