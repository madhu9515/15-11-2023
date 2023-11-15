print('working with tuples')
t=('madhu','sumanth','venkatesh','naveen chand','nikhil','raju','nagarjuna','sandeep')
print(f'created tuple={t}')
print(f'length of given tuple={len(t)}')
print()
print(f'acessing first element={t[0]}')
print(f'acessing second element={t[1]}')
print(f'acessing second element={t[1]}')
print(f'acessing only (m)={t[0][0]}')
print(f'acessing sub string element={t[1:7]}')
print('list of all names in tuple=')
for name in t:
    print(name)
if 'madhu' in t:
    print('madhu is in the in given list')
else:
    print('madhu is not in given list')

