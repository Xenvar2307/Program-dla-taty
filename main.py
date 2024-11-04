import pyperclip

file = open("./res/text-to-copy.txt","r")
text = file.read()

pyperclip.copy(text)