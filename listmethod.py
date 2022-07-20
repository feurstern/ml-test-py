#Method that manipulate data in a list

#Append that method who added a list in last index
userAge = [23,50,40,23,32,67,56]
userAge.append(False)
print("After using append method",userAge)

#insert Inserts an item at the ith position in a list
userAge.insert(7,18)
print("After using insert method", userAge)

#pop remove item from a list
userAge.pop(0)
print("After using pop method:", userAge)

#sort Modifies a list to be sorted
userAge.sort()
print("After using sort method:", userAge)

#reverse
userAge.reverse()
print("After using reverse method:",userAge)

username=input("Enter your name:")
print(len(username))







