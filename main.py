def main():
    bookpath = "books/frankestein.txt"
    text = getbooktext(bookpath)
    counter = counterwords(text)
    print(text)
    print(f"Count of words: {counter}")


def getbooktext(path):
    with open(path) as f:
        return f.read()


def counterwords(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return(counter)
main()