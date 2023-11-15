
def fibonacci(n):
    s1=0
    s2=1
    for b in range(n-2):
        s=s1+s2
        s1=s2
        s2=s
    return s
    
n=int(input('enter a value= '))     
print(fibonacci(n))

        
