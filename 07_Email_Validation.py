# email = input("Enter your Email: ")

email = input("Enter your Email: ")
def emailfun(num):
    k = j = e= False
    l =0
    if len(email) > 6:
        if email.count("@") == 1 and email.count("@")<2:
            if email[0].isalpha():
                if (email[-3] == ".") ^ (email[-4] == "."):
                    if email.count(".") <= 2:
                        for i in email:
                            if i == i.isspace():
                                k = True   
                            elif i.isalpha():
                                if  i == i.upper():
                                    j = True 
                            elif i.isalpha():
                                continue 
                            elif i.isdigit():
                                continue
                            elif(i == "_") or (i == ".")  or (i == "@"):
                                continue
                            else:
                                l = 1           
                        if k or j or l==1 or e:
                            print('Wrong Email')
                        else:
                            print("true email")
                    else:
                        print("Wrong EMAIL.. Please .>1 is not allow ")
                else:
                    print("Wrong EMAIL.. Please enter . correct option")
            else:
                print("Please enter 1st letter (a to z)")
        else:
            print("Cannot enter @>1 OR @<2:")
    else:
        print("Please enter number of letter greater than 6:")


email1 = emailfun(email)