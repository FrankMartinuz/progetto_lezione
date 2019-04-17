import xml.etree as xml

from bin.Lesson import Lesson


def getParam(tag):
    if tag == "link"
        return tree.find(tag).text


f = open('lesson2.xml', 'r')
tree = xml.ElementTree.parse(f)

if __name__ == "__main__":
    l = Lesson()
    tags = ["title", "description", "text", "link"]
    for i in tags:
        print(getParam(i))
