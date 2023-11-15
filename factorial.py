n=5
print('factorial of given number without using recursion')
s=1
for a in range(1,n+1):
    s=s*a
print(s)

print('factorial of given number using recursion')
def fact(n):
    if n==0 or n==1:
        return n
    return n*fact(n-1)
n=10
print(fact(10))
    
