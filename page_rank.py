
import random
from pprint import pprint
no_of_pages=12
"----------------------RANDOM GRAPH-------------"
p={}
q={}
j=0
for i in range(1,no_of_pages):
    p[i]=[]
    q[i]=[]
for i in range(1,no_of_pages):
    random_no=random.randint(1,no_of_pages-1)
    while j<random_no:
        b=random.randint(1,no_of_pages-1)
        if (i!=b and (b not in p[i]) ):
            p[i].append(b)
            q[b].append(i)
        j+=1
    j=0
"-----------------------------------------------------"
"------------------ALGORITHM---------------------------"    
page_rank=0.25
damping_factor=0.85
ans=[]

for i in range(0,len(p)+1):
    ans.append(0.25)
for it in range(10):
    #print("iteration no",it)  
    for i in range(1,len(p)+1):
        ans[i]=0
        for j in q[i]:
            if(i!=j):
                #print("page ",i," is added ",ans[j],len(p[j]))
                ans[i]+=(ans[j]/len(p[j]))
        ans[i]=(((1-damping_factor)/(no_of_pages-1))+(damping_factor*ans[i]))       
    #for i in range(no_of_pages):
         
    #print("Answer=",ans," and sum= ",sum(ans)-0.25)  
            #print(q,i,j)
   # print("next")   
print("Answer=",ans," and sum= ",sum(ans)-0.25)  












        

                    
