
import string
def filemanager():
    o = open("napolean.txt", "r")
    text = o.read()
    return text


def frequency(word):
    print word
    text = filemanager()
    new_text = string.split(text)
    res = [1 for something in new_text if something.lower() == word.lower()]
    z = 0
    if len(res) > 0:
        z = reduce(lambda x, y: x + y, res)
    return z

#words is a list of words
def tot_frequency(words):
    return reduce(lambda x,y: x+y, [ frequency(word) for word in words ])

print frequency("the")
print tot_frequency(["the", "apple"])
print tot_frequency(["the", "miserable"])
