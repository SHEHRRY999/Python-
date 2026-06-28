def Code():
    sentence = str(input("Enter A Sentence : "))
    words = sentence.split()
    start = "kbg"
    stop = "pko"
    coded = ""
    for word in words:
        if len(word) >= 3:
            new = word[1:] + word[0]
            newword = start + new + stop
            coded = coded + newword + " "
        else:
            coded = coded + word[::-1] + " "
    return coded


def DeCode():
    sentence = str(input("Enter The Sentence to Decode : "))
    words = sentence.split()
    decoded = ""
    for word in words:
        if len(word) >= 3:
            new = word[3:-3]
            newword = new[-1] + new[:-1]
            decoded = decoded + newword + " "
        else:
            decoded = decoded + word[::-1] + " "
    return decoded


Coded_Sentence = Code()
print("Coded Sentence: ", Coded_Sentence)
DeCoded_Sentence = DeCode()
print("DeCoded Sentence: ", DeCoded_Sentence)

