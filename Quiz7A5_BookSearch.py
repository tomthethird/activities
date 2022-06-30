book = True
# bookinit = open("books.dat", "x")
# bookinit.close()
while book:
    choice = int(input("\n1. Add Record\n2. Display Record\n3. Search a Record\n4. Exit\nEnter choice(1-4): "))
    while True:
        if choice == 1:
            addBook = True
            while addBook:
                print("\nADD RECORD")
                bookID = input("Enter book ID: ")
                bookTitle = input("Enter book title: ")
                bookCat = input("Enter category: ")
                bookAuthor = input("Enter author: ")
                save = input("SAVE? Y/N: ")

                if save.lower() == "y":
                    outbook = open("books.dat", "ab+")
                    bookdata = (outbook.read()).decode("utf-8").lower()
                    idloc = bookdata.find(bookID)

                    if idloc > 0:
                        bookrecord = f"\nID: {bookID}\nBook Title: {bookTitle}\nCategory: {bookCat}\nAuthor: {bookAuthor}\n"
                        outbook.write(bookrecord.encode("utf-8"))
                        outbook.close()
                        print("\nBook saved.")
                        addBook = False
                    else:
                        print("\nRecorded ID. Please use different ID.")
                        addBook = False

                elif save.lower() == "n":
                    print("\nBook not saved.")
                    break
                else:
                    print("\nInvalid input.")
                    addBook = False
            break

        elif choice == 2:
            print("\nDISPLAY RECORD")
            inbook = open("books.dat", "rb")
            bookdata = (inbook.read()).decode("utf-8")
            print(bookdata)
            print("")
            inbook.close()
            break

        elif choice == 3:
            print("\nSEARCH A RECORD")
            inbook = open("books.dat", "rb")
            bookdata = (inbook.read()).decode("utf-8").lower()
            bookOpen = True
            while bookOpen:
                searchChoice = int(input("1. Search via ID\n2. Search via Book Title\nEnter choice(1 or 2): "))

                while searchChoice != 1 or searchChoice !=2:
                    if searchChoice == 1:
                        searchinput = input("Enter Book ID: ")
                        break
                    elif searchChoice == 2:
                        searchinput = input("Enter Book Title: ").lower()
                        break
                    else:
                        print("\nInvalid input.\n")
                        searchChoice = int(input("Enter choice(1 or 2): "))

                booklocation = bookdata.find(searchinput)

                if booklocation > 0 and searchChoice == 1:
                    booklocation -= 4
                    bookOpen = False
                elif booklocation > 0 and searchChoice == 2:
                    booklocation -= 21
                    bookOpen = False
                else:
                    print("\nRecord not found.\n")

            result = inbook.seek(booklocation)
            
            line1 = (inbook.readline(result)).decode("utf-8")
            line2 = (inbook.readline(result+1)).decode("utf-8")
            line3 = (inbook.readline(result+2)).decode("utf-8")
            line4 = (inbook.readline(result+3)).decode("utf-8")
            print(f"\n{line1}{line2}{line3}{line4}")
            inbook.close()
            break

        elif choice == 4:
            print("\nExit\n")
            book = False
            break

        else:
            print("\nInvalid input.")
            break