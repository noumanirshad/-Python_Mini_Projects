list = []
print("\t********Welcome to Afaq genral store********\n")
sum = 0
userinput = None
while(userinput != 'q'):
    print("Press q to exit the program")
    userinput = (input("Enter the price: "))
    if(userinput != 'q'):
        sum = sum + int(userinput)
        list.append(userinput)
        print(f"\nYour amount still at this time: {sum}\n\tYour item list is {list}\n")
        
    else:
        print("\t********Thank you so Much for comming here\n")
        
        