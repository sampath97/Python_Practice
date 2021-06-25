#Program to print nth fibonacci number
def get_fib(n):
    first =0
    second=0
    current=1
    fib_list=[current]
    for item in range(1,n):
        first=second
        second=current
        current=first+second
        fib_list.append(current)
        
    return(fib_list)

    
#Print the nth fibonacci number
x=int(input("Enter index of fibonacci number: "))
fib_list=get_fib(x)
print(fib_list[x-1])
    


    
