import math
from math import pow
import random
from pprint import pprint
no_of_pages=30
"----------------------RANDOM GRAPH-------------"
p={}
q={}
j=0
for i in range(1,no_of_pages):
    p[i]=[]
    q[i]=[]
for i in range(1,no_of_pages): #why not the last page
    random_no=random.randint(1,no_of_pages-1)
    while j<random_no:
        b=random.randint(1,no_of_pages-1)
        if (i!=j and (b not in p[i]) ):
            p[i].append(b)
            q[b].append(i)
        j+=1
    j=0
"-------------------------Algorithm---------------"
auth={}
hub={}

for i in range(1,no_of_pages):
    auth[i]=1
    hub[i]=1
for i in range(10):
    norm=0
    for j in range(1,no_of_pages):
        auth[j]=0 
        for m in q[j]:
            auth[j]=auth[j]+hub[m]
        norm+=pow(auth[j],2)
    norm=math.sqrt(norm)
    for i in range(1,no_of_pages):
        auth[i]=auth[i]/norm
    norm=0
    for j in range(1,no_of_pages):
        hub[i]=0
        for m in p[j]:
            hub[j]+=auth[m]
        norm+=pow(hub[j],2)
    norm=math.sqrt(norm)
    for i in range(1,no_of_pages):
        hub[i]=hub[i]/norm

for i in range(1,no_of_pages):
    print(hub[i],)
print("")
for i in range(1,no_of_pages):
    print(auth[i])    
            
    
        
