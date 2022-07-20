print("Triangle Program")

def pyramid():
    rows=int(input("Enter a row:"))

    for i in range(rows):
        for j in range(i):
            print(i, end='')
        
        print('')

def pyramid2():

    rows= int(input("Enter your number:"))
    
    for i in range(1,rows+1):
        for j in range(1,i+1):
            print(j,end="")
        print("")

pyramid()
pyramid2()