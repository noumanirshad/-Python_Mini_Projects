class Laibrary:
    def __init__(self, list, name):
        self.booklist = list
        self.LaibraryName = name
        self.landDict = {}

    def Displaybook(self):
        print(f"\t\t***** Welcome to {self.LaibraryName}\n\t There are following books in this laibrary. *****")
        for books in self.booklist:
            print(books)

    def lendbook(self, book, user):
        if book in self.booklist:
            self.booklist.remove(book)
            self.landDict.update({book: user})
            print(
                f"\t\t\n***** Suceessfully: Now you can take this book: ('{book}') *****\n")
        else:
            print("\t\t\n***** Sorry: This book is not be available at this time *****\n")

    def addbook(self, book):
        self.booklist.append(book)
        print("\t\t\n***** Your book has been added ***** \n")

    def returnbook(self, book, user):
        self.landDict.pop(book)
        print("\t\t\n***** Return sucessfully: Thank You so much ***** \n")

    def checkstatus(self):
        print(
            f"\t\t\n***** These books has been booked  *****  \n{self.landDict}\n ")


if __name__ == "__main__":
    numi = Laibrary(['Python', 'C++ Basic', 'Java', 'C_sharp',
                    'Data Science'], "Preston Laibrary")
    user = 0

    while(user != 6):
        try:
            print("\t *****************")
            print("Choice in 1 option")
            print("1: DisplayBook")
            print("2: LendBook")
            print("3: AddBook")
            print("4: ReturnBook")
            print("5: Check Status")
            print("6: Exit")
            user = int(input("Enter your chioce: "))
            if (user == 1):
                numi.Displaybook()
                print('\n')
            elif(user == 2):
                book = input("Enter your book name: ")
                username = input("Enter your name: ")
                numi.lendbook(book, username)
            elif(user == 3):
                book = input("Enter your book name: ")
                numi.addbook(book)
            elif(user == 4):
                book = input("Enter your book name: ")
                username = input("Enter your name: ")
                numi.returnbook(book, username)
            elif(user == 5):
                numi.checkstatus()
            elif (user == 6):
                print("\t\t\n*****Thank you for using  *****\n")
        except:
            print("\t\t\n*****Please: Enter the valid option  *****\n")
