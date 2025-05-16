# practice
#1
a=5
rem=""
while a: #we will iterate loop untill a bocome 0
   rem+=str(a%2)
   a=a//2
print(rem[::-1])                                    
#2
a="101"
dec=0
a=a[::-1] 
for i in range(len(a)):
    dec+=int(a[i])*(2**i)
print(dec)
#convert dec to binay by using bitwise operators
#count bits in a binary digit
#3
a=8
count=0
while a:
     a=a>>1
     count+=1
print(count)    
 # count set bits 4
a=5
count=0
while a:
     if a&1==1: 
         count+=1
     a=a>>1
print(count) 
#count reset bits 5
a=8
count=0
while a:
    if a&1!=1:
        count+=1
    a=a>>1
print(count)
#find first set bit from  right side 6
a=16
count=0
while a&1==0:
    count+=1
    a=a>>1
print(count)
#find first reset bit from right side 7
a=16                
count=0
while a&1!=0:
    a=a>>1
    count+=1
print(count)
#find first set bit from left side 8
a=8
while a&1==0:
    a=a>>1
    count+=1
print(count)
    
    
 #ith element 9
def fun(a,i):
    mask=1<<i       
    mask=~mask
    return a&mask 
print(fun(5,0)) 
#a=8 1000
#set 1 in the ith bit 1100
              #1
              #1100 output:1100 10
def fun(a,i): 
    mask=1<<i
    return a|mask
print(fun(8,2)) # i =2  is the ith position


#1 0 1 0
#0 1 0 0 perform and operation 0 0 0 0 everything is 0 then that particular position also 0 if any value there is a 1
def fun(a,i): #1000 &1<<i 1000&0100 =0000 return 0 11
    mask=1<<i
    return int(mask&a>0)    
print(fun(8,2)) 
#power of 2 12
def fun(a):
    return  a&a-1==0
print(fun(8))
#fing unique value in a list 13
a=[3,4,3,4,9]
res=0
for i in a:
  res^=i
print(res)
#14
def clear(a,i):
    mask=1<<i
    mask=~mask
    return a&mask
print(clear(8,2))
print(5//2)
a=5
print(a%2)
#
a=5
rem=""
while a :
   rem+=str(a%2)
   a=a//2
print(rem)
#
a="101"
dec=0
a=a[::-1]
for i in range(len(a)):
    dec+=int(a[i])*(2**i)
print(dec)
#
