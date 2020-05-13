userinput = input("Username : ")
passinput = input("Password : ")
if userinput == "siwakorn" and passinput == "0000":
    print("Success ! Hi",userinput,". :D")
    print("1. Apple      x1 | 15 Baht")
    print("2. Banana     x1 | 10 Baht")
    print("3. Mango      x1 | 30 Baht")
    print("4. Strawberry x1 | 5  Baht")
    userselected = int(input("Enter number >> "))
    uservolume = int(input("How many do you want >> "))
    print("----- Order -----")
    if userselected == 1:
        print("Apple  x",uservolume,"  total :",uservolume*15,"Baht")
    elif userselected == 2:
        print("Banana  x", uservolume, "  total :", uservolume * 10, "Baht")
    elif userselected == 3:
        print("Mango  x", uservolume, "  total :", uservolume * 30, "Baht")
    elif userselected == 4:
        print("Strawberry  x", uservolume, "  total :", uservolume * 5, "Baht")
    else:
        print("Sorry ! This number no have in stock.")
else:
    print("Error! Please try again")