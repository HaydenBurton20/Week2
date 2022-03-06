rentOldies = 2
rentNew = 3
oldies = float(input("Enter how many old videos you are renting: "))
new = float(input("Enter how many new videos you are renting: "))
totalcost= oldies * rentOldies + new * rentNew
print("The total cost is $" + str(totalcost))
