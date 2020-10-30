txt = input("enter a text: ")
words = txt.split()
longest =  len(words[1])
for i in words:
    wordlength = len(i)
    if wordlength > longest:
        longest = wordlength
        currentword = i

print("longest word is: ",currentword)
print("length: ",wordlength)
