#Python program to check if a number is Armstrong number/not

x=int(input("Enter number: "))

y=x
as_sum=0
count=0

while(y>0):
    r=y%10
    count=count+1
    y=y//10
    
y=x
    
while(y>0):
    r=y%10
    as_sum=as_sum+pow(r,count)
    y=y//10


if(as_sum==x):
    print("Armstrong number")
else:
    print("Not armstrong")
    

