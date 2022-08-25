from locale import currency


with open("currency.txt") as f:
    lines = f.readlines()
currencydict = {}
for line in lines:
    split = line.split("\t")
    # currencydict[split[0]] = split[1]
    currencydict.update({split[0]:split[1]})
amount = int(input("Enter amount: \n"))
print("Enter the name of currency you want to convert this amount to? Available option are: \n")
for cur in currencydict.keys():
    print(cur)
currency = input("Enter amount: \n")
print(f"{amount} PKR is equal to {amount *float(currencydict[currency])} {currency}")