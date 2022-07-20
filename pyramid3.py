#inverted downward pattern

rows = int(input("Enter a number for rows:"))
a=0;

for i in range(rows,0,-1):
    a+=1
    for j in range(1,i+1):
        print(a,end='')
    print('')