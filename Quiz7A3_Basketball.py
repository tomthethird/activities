import pickle

def basketball(file):
    basketlist = ""
    infile = open(file, "rb")
    while True: #read to the end of file.
        try:
            participant = pickle.load(infile) #reading the oject from file
            if participant[0] == "Basket Ball":
                basketlist += f"{participant[0]} {participant[1]}\n"
        except EOFError: 
            break
    infile.close() #close the file

    outfile = open("basket.dat", "wb")
    outfile.write(basketlist.encode())
    outfile.close()

basketball("game.dat")