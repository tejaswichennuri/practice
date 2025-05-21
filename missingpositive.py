l=[1,2,0,3,5]
for i in l:
    if i==0:
        l.remove(0)
        l.append(0)
print(l)
#remove even
l=[1,3,6,4,5,8] #indexes 0 1 2 3 4 5
k=0
for i in range(len(l)):
    if l[i]%2!=0:
     temp=l.pop(i)
     l.insert(k,temp)
     k+=1
print(l)
#remove zero's
l=[1,2,0,3,0,5]
for i in l:
    if i==0:
        l.remove(0)
        l.append(0)
print(l)
        
    
    


             
    