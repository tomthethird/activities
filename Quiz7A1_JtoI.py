f = open("WORDS.txt", "w")
f.write("WELL, THJS JS A WORD BY JTSELF. YOU COULD STRETCH THJS TO BE A SENTENCE")
f.close()
f = open("WORDS.TXT", "rt")
print(f.read())
f.close()

def JTOI(file):
    f = open(file, "rt")
    text = f.read() 
    text = text.replace("J","I") #store the edited texts
    f.close()

    f = open(file, "w")
    f.write(text) #rewrite the edited text to the file
    f.close()

JTOI("WORDS.TXT")

f = open("WORDS.TXT", "rt")
print(f.read())
f.close()