menuList = []

def showBill():
    total = 0
    print("---- My Food ----")
    for i in range(len(menuList)):
        print(menuList[i][0],menuList[i][1])
        total += int(menuList[i][1])
    print("Total :",total)
while True:
    menuName = input("Please enter menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price :")
        menuList.append([menuName,menuPrice])
showBill()