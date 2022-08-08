from PyPDF2 import PdfReader
import os
from _collections import OrderedDict
import matplotlib.pylab as plt

name = None
for i in os.listdir():
    if str(i).endswith(".pdf"):
        name = str(i)

try:
    reader = PdfReader(name)
except AttributeError:
    input("DOWNLOAD THE PDF FILE OF THE BOOK YOU WANT AND COPY IT TO THIS FOLDER")
    quit()

pages = len(reader.pages)
words = {}

for page in range(len(reader.pages)):
    if os.name == "nt":
        os.system("cls")
    if os.name == "posix":
        os.system("clear")

    print("{}/{}".format(page + 1, pages))
    text = reader.pages[page].extract_text()
    for word in text.split():
        word = word.lower().strip()
        word = word.replace(".", "")
        word = word.replace(",", "")
        word = word.replace("!", "")
        word = word.replace('"', "")
        word = word.replace("“", "")
        word = word.replace("”", "")
        word = word.replace("-", "")
        word = word.replace("–", "")
        word = word.replace(")", "")
        word = word.replace("(", "")
        word = word.replace(";", "")
        word = word.replace(":", "")
        word = word.replace("?", "")

        try:
            word.split("'")[1]
            word = word.split("'")[0]
        except IndexError:
            pass
        try:
            word.split("’")[1]
            word = word.split("’")[0]
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

words_sorted = {k: v for k, v in sorted(words.items(), key=lambda item: item[1])}
words_sorted_reversed = dict(OrderedDict(reversed(list(words_sorted.items()))))

limit = input("How many words do you want to see? ")
try:
    limit = int(limit)
except ValueError:
    input("JUST ENTER NUMBERS. EXAMPLE: 10")
    quit()

most_used = {}
a = 0
for i in words_sorted_reversed:
    a += 1
    print("{}. {} => {}".format(a, i, words_sorted_reversed[i]))
    most_used[words_sorted_reversed[i]] = i
    if a == limit:
        break

a = most_used.items()
a = sorted(a)
x, y = zip(*a)
plt.plot(x, y)
plt.show()