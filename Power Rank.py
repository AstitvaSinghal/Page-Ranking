import random
from pprint import pprint
import math
no_of_pages=100

"-----------------RANDOM GRAPH---------------"
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
#print p
#print q

"-------------------------Algorithm---------------"
t=0
beta=0.5
gamma=0.5

P=[]
PN=[]
for i in range(1,no_of_pages+1):
    P.append(0)
    PN.append(0)

while(t<10):
    alpha=math.exp(-1*beta*t)
    #print alpha,
    t+=1
    for j in range(1,no_of_pages):
        mx=-1
        for i in q[j]:
            iu=len(q[i])
            ou=len(p[i])
            #print i,iu,ou
            f=math.pow(2,(1.0*iu/ou))+gamma*P[i]
            if(f>mx):
                mx=f
        PN[j]=(1-alpha)*P[j]+alpha*mx
    for i in range(1,no_of_pages-1):
        P[i]=PN[i]
    #print PN
PN.sort()
print PN
    
        

