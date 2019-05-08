from bin.user import User


class Student(User):
    def __init__(self):
        User.__init__(self)
        self.__class = None
        self.__id_student = None

    def chooseSubject(self, entry_first_name, entry_last_name):
        self.set_first_name(entry_first_name.get())
        self.set_last_name(entry_last_name.get())


    def doQuiz(self):
        return

    def set_first_name(self, first_name):
        self._first_name = first_name

    def set_last_name(self, last_name):
        self._last_name = last_name


if __name__ == "__main__":
    a = Student()
    print(a.__dict__)
