def main():
    bookpath = "books/frankestein.txt"
    text = getbooktext(bookpath)
    counter = counterwords(text)
    counterch = countercharacters(text)
    reportbook(bookpath, counter, counterch)


def getbooktext(path):
    with open(path) as f:
        return f.read()


def counterwords(text):
    words = text.split()
    counter = 0
    for word in words:
        counter += 1
    return(counter)

def countercharacters(text):
    countofcharacters = {
        "a": 0, "b": 0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0, 
        "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0,
        "u":0, "v":0, "w":0, "x":0, "y":0, "z":0
    }
    low = text.lower()
    
    for character in low:
        if character in countofcharacters:
            countofcharacters[character] += 1

    return countofcharacters

def reportbook(path, countwd, countch):
    print("         REPORT")
    print("-------------------------")
    print(path)
    print()
    print(f"{countwd} words were found")
    for ch in countch:
        num = countch.get(ch)
        print(f"The '{ch}' character was found {num} times")
    print("-------------------------")
    print("         END REPORT")

main()     