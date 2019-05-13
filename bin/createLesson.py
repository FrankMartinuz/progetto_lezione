from bin.lesson import Lesson
import xml.etree.ElementTree as xml

def loadId():
    tree = xml.parse("..\config\config.xml")
    root = tree.getroot()
    for tag in root.iter("idLesson"):
        id = int(tag.attrib.get("id"))
        print(id)
        tag.set("id","" + str(id+1))
    tree.write('..\config\config.xml')
    return id

if __name__ == "__main__":
    title = input("Inserire titiolo della lezione:")
    desc = input("Inserire descrizione della lezione:")
    text = input("Inserire testo della lezione:")
    n = " "
    link = []
    while (n != ""):
        n = input("Inserire eventuali link per la lezione:")
        link.append(n)
    id = loadId()
    l = Lesson(title, desc, text, link, id)
    l.createLesson()
    print(l.showLesson())
