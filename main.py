
import string
def filemanager():
    o = open("napolean.txt", "r")
    text = o.read()
    return text

def filemanager2():
    o = open("n.txt", "r")
    text = o.read()
    return text

def frequency(word):
    text = filemanager()
    new_text = string.split(text)
    res = [1 for something in new_text if something.lower() == word.lower()]
    z = 0
    if len(res) > 0:
        z = reduce(lambda x, y: x + y, res)
    return z
    "Adds one whenever a words is detected"

#words is a list of words
def tot_frequency(words):
    return reduce(lambda x,y: x+y, [ frequency(word) for word in words ])
    "Takes the words and finds the freqency of each words"

def most_freqency():
    text = filemanager2()
    new_text = string.split(text)
    return reduce( lambda x,y: x if x > frequency2(y) else frequency2(x), new_text)
    "Takes 2 words, finds their frequency and compares them. The highest freqency stays, and moves to next word."

def filemanager2():
    o = open("n.txt", "r")
    text = o.read()
    return text

def frequency2(word):
    text = filemanager2()
    new_text = string.split(text)
    res = [1 for something in new_text if something.lower() == word.lower()]
    z = 0
    if len(res) > 0:
        z = reduce(lambda x, y: x + y, res)
    return z
    "Adds one whenever a words is detected"

print most_freqency()
print frequency("the")
print tot_frequency(["the", "apple"])
print tot_frequency(["the", "miserable"])
