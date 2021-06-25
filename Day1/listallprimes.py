#Print all prime numbers in an interval

x,y=input("Enter limits of range(x ,y): ").split()
x=int(x)
y=int(y)

z=range(x+1,y)

def isprime(x):
    for item in range(2,(x//2)+1):
        if x%item==0:
            return 0
    
    return 1
    

for item in z:
    pr=isprime(item)
    if pr==1:
        print(item,end=" ")
    
    
