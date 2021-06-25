#Python program to find factorial of a number

x=int(input('Enter number: '))


def getfactorial(y):
    if y==0 or y==1:
        return 1
    elif y<0:
        return 0
    else:
        return (y*getfactorial(y-1))
    


y=getfactorial(x)

print('factorial of {} is {}'.format(x,y))