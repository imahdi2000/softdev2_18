
import string
def filemanager():
    o = open("napolean.txt", "r")
    text = o.read()
    return text


def freqency(word):
    text = filemanager()
    new_text = string.split(text)
    z = reduce(lambda x, y: x + y, [1 for something in new_text if something == word])
    print z


freqency("apple")
