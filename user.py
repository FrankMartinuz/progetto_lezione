from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self):
        self._first_name = ""
        self._second_name = ""
        self._id = None
        self._password = None

    @abstractmethod
    def chooseSubject(self, subject):
        self.__subject = subject
