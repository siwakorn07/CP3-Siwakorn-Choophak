menuList = []
priceList = []

def showBill():
    total = 0
    print("---- My Food ----")
    for i in range(len(menuList)):
        print(menuList[i],priceList[i])
        total += int(priceList[i])
    print("Total :",total)
while True:
    menuName = input("Please enter menu :")
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append((menuPrice))
showBill()