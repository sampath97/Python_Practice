#Program to rotate an array by d elements

n=int(input("Enter size of array: "))

arr_list=[]

print("Enter array elements: ")
for item in range(0,n):
    x=int(input())
    arr_list.append(x)
    
   
ns=int(input("Enter number of elements to be rotated: "))
    
i=1
while(i<=ns):
    for item in range(0,n-1):
        temp=arr_list[item]
        arr_list[item]=arr_list[item+1]
        arr_list[item+1]=temp
    i=i+1
        
print(arr_list)


