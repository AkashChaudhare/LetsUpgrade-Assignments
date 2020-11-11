#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#question 1
lll=list()
count=0
x=0
while x==0:
    i=int(input())
    if (i%2==0):
        lll.append(i)
        count+=1
        if count==10:
            break
    


# In[ ]:


#question 2
a=list()  #empty list
for i in range(5):
    a.append(i)
print(a)
b=list(range(6))
print(b)
b.pop()
b.remove(3)
print(b)
b.sort(reverse=True)
print(b)
b[3]=15
print(b)


# In[ ]:


#question 3
n=int(input())
ddd=dict()
for i in range(n):
    ddd[i]=i*i
print(ddd)


# In[2]:


#question 4
x,y=0,0
print("Enter 0 to exit")
print("Enter 2 to give directions for right and up")
print("Enter 4 to give directions for all 4 directions")
n=int(input(""))
while True:
    if n==0:
        print("No change in position")
        p,q,r,s=0,0,0,0
        break
    elif n==2:
        p=float(input("UP "))
        s=float(input("RIGHT "))
        q,r=0,0
        break
    elif n==4:
        p=float(input("UP "))
        q=float(input("DOWN "))
        r=float(input("LEFT "))
        s=float(input("RIGHT "))
        break
    else:
        print("Try again")
        pass
        

y+=(p-q)
x+=(s-r)
dis=int(round((x**2 + y++2)**(1/2)))

print("Distance=",dis)


# In[ ]:




