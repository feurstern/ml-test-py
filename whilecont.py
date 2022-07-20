# A shop is running a promotion today! If an item's price is an odd number, you get that item for free!
# You use a list to store the prices of all items in the shopping cart.
# The given code uses a while loop to iterate over the list, calculates the price of all the items in the list, and output the result.
# Change the code to skip the odd prices, calculate the sum of only the even prices and outputs the result


itemPrice=[20,15,40,17,26,64]
sum= 0
n = 0
while n<len(itemPrice):
    num = itemPrice[n]
    n+=1
    if num %2!=0:
        continue
    sum+=num

print("Your cart is:",sum)



