from PyPDF2 import PdfReader
import os
from _collections import OrderedDict
import matplotlib.pylab as plt
import sys

name = None
for i in os.listdir():
    if str(i).endswith(".pdf"):
        name = str(i)

try:
    reader = PdfReader(name)
except AttributeError:
    input("DOWNLOAD THE PDF FILE OF THE BOOK YOU WANT AND COPY IT TO THIS FOLDER")
    sys.exit()

pages = len(reader.pages)
words = {}
chars = [".", ",", "!", '"', "“", "”", "-", "–", ")", "(", ";", ":", "?"]
chars2 = ["'", "’"]

for page in range(len(reader.pages)):
    if os.name == "nt":
        os.system("cls")
    if os.name == "posix":
        os.system("clear")

    print("{}/{} {}%".format(page + 1, pages, int(((page+1)/pages)*100)))
    text = reader.pages[page].extract_text()
    for word in text.split():
        word = word.lower().strip()
        for i in chars:
            word = word.replace(i, "")

        for i in chars2:
            try:
                word.split(i)[1]
                word = word.split(i)[0]
            except IndexError:
                pass

        if not word in words:
            if len(word) < 2:
                continue
            try:
                int(word)
                pass
            except ValueError:
                clean = True
                for i in range(10):
                    if str(i) in word:
                        clean = False
                if clean:
                    words[word] = 1
        else:
            words[word] = words[word] + 1

del chars
del chars2
del pages
del name
del reader

words_sorted = {k: v for k, v in sorted(
    words.items(), key=lambda item: item[1])}
words_sorted_reversed = dict(OrderedDict(reversed(list(words_sorted.items()))))

del words_sorted

limit = input("How many words do you want to see? ")
try:
    limit = int(limit)
except ValueError:
    input("JUST ENTER NUMBERS. EXAMPLE: 10")
    sys.exit()

most_used = {}
a = 0
for i in words_sorted_reversed:
    a += 1
    print("{}. {} => {}".format(a, i, words_sorted_reversed[i]))
    most_used[words_sorted_reversed[i]] = i
    if a == limit:
        del a
        break

del words_sorted_reversed
del limit

a = most_used.items()
a = sorted(a)

del most_used

try:
    x, y = zip(*a)
except ValueError:
    input("UNKNOWN ERROR")
    sys.exit()

del a

#plt.plot(x, y)
plt.bar(y, x, width=40, color="cyan")
plt.show()
