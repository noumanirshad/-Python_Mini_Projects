class Train:

    def __init__(self, name, fear, seats):
        self.name = name
        self.fear = fear
        self.seats = seats
        self.dict = {}

    def getstatus(self):
        print(f"\n\tThe name of train is {self.name}")
        print(f"\tAvailable seats are {self.seats}")
        print(f"\tThe fear of train is {self.fear}")
        print(f"\n\t****These seats have been booked: \n\t\t****{self.dict}")

    def bookticket(self, user):
        if (self.seats > 0):
            self.dict[user] = self.seats
            # self.dict.update({user: self.seats})
            self.seats = self.seats - 1
        else:
            print("\n\tSorry; Train is full please try in other train:")

    def cancleticket(self):
        name = input("\tEnter your name: ")
        if (name in self.dict):
            print("\n\t***** Your ticket has been cancled")
            self.dict.pop(name)
            self.seats = self.seats+1
        else:
            print("Sorry:You ticket do not book.")


if __name__ == "__main__":
    numi = Train("Allama Iqbal Express (9 Up/10 Dn) ...", 500, 10)
    user = 0

    while(user != 4):
        try:
            print(f"\n....welcome to the '({numi.name})'.......")
            print(" press 1 for Check_getstatus...")
            print(" press 2 for Book_Ticket......")
            print(" press 3 for Cancle_Ticket.....")
            print(" press 4 for Exit.....")
            user = int(input("Enter your chioce: "))
            if(user == 1):
                numi.getstatus()
            elif(user == 2):
                name = input("\tEnter your name: ")
                print(f"\n\t***** Your ticket has been booked.")
                print(f"\t***** Seat no of '{name}' is '{numi.seats}'")
                numi.bookticket(name)
            elif(user == 3):
                numi.cancleticket()
            elif(user == 4):
                print(f"\n\tThank you for using {numi.name} Train")
            else:
                print("Please: Enter valid option: ")

        except:
            print("Please: Enter valid option: ")

