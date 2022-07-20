def userGreeting(username):
    username=input("Input your name:")
    print("Hello, " ,username,"!")

def pytagoras(a,t):
    m= 0.5*a*t
    print(m)

def calc(x,y):
    print(x+y)

def max(x,y):
    if x>=y:
        return x
    else:
        return y

userGreeting("username")
pytagoras(10,4)
calc(6,112)
print(max(2,4))
x=max(7,3)
print(x)