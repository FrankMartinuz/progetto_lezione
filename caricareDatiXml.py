import xml.etree as xml

from lesson import Lesson


def getParam(tag):
    if tag == "link":
        vett = []
        link = tree.find(tag)
        for i in range(len(link)):
            vett.append(link.find("L" + str(i)).text)
        return vett
    else:
        return tree.find(tag).text


f = open('lesson5.xml', 'r')
tree = xml.ElementTree.parse(f)

if __name__ == "__main__":
    for node in tree.getiterator('lesson'):
        id = node.attrib.get('id')
    l = Lesson(getParam("title"), getParam("description"), getParam("text"), getParam("link"), id)
    l.createLesson()
