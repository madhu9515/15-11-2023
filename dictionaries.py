print("working with dictionaries")
D={'a':10,'b':20,'c':30,'d':40,'e':50}
print('created dictionary=',D)
D['f']=60
print('updated dictionaries=',D)
print('only keys in dicts=')
for items in D:
    print(items)
print('only values in dicts=')
for values in D:
    
    print(D[values])

print('created dictionary',D)
print('acessing first values of (a)',D.get('a'))
print('delete all elements in dictionaries=',D.clear())
print('after deleted elements=',D)



