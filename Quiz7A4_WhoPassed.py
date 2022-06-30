import pickle

def count_rec(file):
    counter = 0
    infile = open(file, "rb")
    while True: #read to the end of file.
        try:
            student = pickle.load(infile) #reading the oject from file
            if student[2] > 75:
                counter += 1
                print(student[0], student[1], student[2])
        except EOFError: 
            break
    return counter
    infile.close() #close the file

studentPass = count_rec("student.dat")
print(f"\n{studentPass} student/s scored > 75.")