from lesson import Lesson

if __name__ == "__main__":
    title = input("Inserire titiolo della lezione:")
    desc = input("Inserire descrizione della lezione:")
    text = input("Inserire testo della lezione:")
    n = " "
    link = []
    while (n != ""):
        n = input("Inserire eventuali link per la lezione:")
        link.append(n)
    l = Lesson(title, desc, text, link)
    l.createLesson()
    print(l.showLesson())
