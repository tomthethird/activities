f = open("notes.txt", "w")
f.write("India is the fastest-growing economy. India is looking for more investments around the globe. The whole world is looking at India as a great market. Most Indians can foresee the heights that India is capable of reaching.")
f.close()

def count_words(file):
    f = open(file, "rt")
    text = f.read().lower()
    f.close()
    result = text.count("the")
    return result
    
print(count_words("notes.txt"))