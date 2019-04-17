# --IMPORT

import xml.etree.cElementTree as xml

# --VARIABLES

boolD = True


# --CLASSE

class Lesson:

    def __init__(self, title="titolo", desc="descrizione", text="testo", link=["link1"], idLesson=-1):
        self.__id_lesson = idLesson
        self.__title = title
        self.__description = desc
        self.__lesson_text = text
        self.__link = link

    def __str__(self):
        return [self.__id_teacher, self.__id_lesson, self.__description, self.__link]

    def setIdTeacher(self, id):
        self.__id_teacher = id

    def getIdTeacher(self):
        return self.__id_teacher

    def setIdLesson(self, id):
        self.__id_lesson = id

    def getIdLesson(self):
        return self.__id_lesson

    def setDescription(self, d):
        self.__description = d

    def getDescription(self):
        return self.__description

    def getLink(self):
        return self.__link

    def setLink(self, array):
        self.__link = array

    def createLesson(self):
        """
        Crea il file .xml con i dati inseriti
        :return: None
        """
        root = xml.Element("lesson", id=str(self.__id_lesson))
        xml.SubElement(root, "title").text = self.__title
        xml.SubElement(root, "description").text = self.__description
        xml.SubElement(root, "text").text = self.__lesson_text
        link = xml.SubElement(root, "link")
        for i in range(len(self.__link)):
            xml.SubElement(link, "L" + str(i)).text = self.__link[i]
        tree = xml.ElementTree(root)
        tree.write("lesson" + str(self.__id_lesson) + ".xml")

    def showLesson(self):
        """
        Stampa la lezione divisa per tag
        :return: string
        """
        lesson = ""
        lesson += self.__title + "\n\n"
        lesson += self.__description + "\n"
        lesson += self.__lesson_text + "\n"
        lesson += self.getLink()
        return lesson

    def getTag(self, tag_to_find):
        """
        Ritorna il contenuto del tag che viene passato come parametro
        :param tag_to_find: string ; Il tag che viene cercato nel file .xml
        :return: string
        """
        tree = xml.parse("lesson" + str(self.__id_lesson) + ".xml")
        root = tree.getroot()
        for tag in root:
            if tag.tag == tag_to_find:
                return tag.text

    def getLink(self):
        string = ""
        for i in self.__link:
            string += i + "\n"
        return string
