for num in range(0,21):
    t=0
    if num<=1:
        t=1
    for x in range(2,num):
        if num%x==0:
            t=1
            break
    if t==0:
        print(num)
    
            
