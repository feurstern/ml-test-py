
myFavourite = ["Germany", "Japan", "New Zealand"]
print(myFavourite)
myFavourite.append("United Kingdom")
sizeMyFavourite = len(myFavourite)
print("After adding using append method become:",myFavourite)


myIdNumber = "ACf123M12C"
hasContainMyFavourite = "Japan" in myFavourite

print(hasContainMyFavourite)

if(hasContainMyFavourite == True):
    print("Congralutaions, we will go to Japan next years")
else:
    print("Sorry, we don't have any further information")


if(myIdNumber.startswith("ACB")):
    print('Welcome, your ID is valid')
else:
    print("Your ID is invalid!")


if(sizeMyFavourite<=5):
    print("Please add more Country!")

else:
    print("The inserted data of countries are enough!")


for i in range(0,5):
    print(i,"I will become an IT expert within two years and already married")

