import random
import math
from pprint import pprint
"----------------------RANDOM GRAPH-------------"
no_of_pages=1000
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
"------------------ PAGE RANK ALGORITHM---------------------------"    
#page_rank=0.25
damping_factor=0.85
#ans=[]
#prob=[]
#epsila=random.uniform(0,0.0005)
#condition=True;
#it=0
#for i in range(0,len(p)+1):
#    ans.append(0.25)
#    prob.append(0)
#while(condition):
##    print(epsila)
##    print("Iteration",it)
#    for i in range(1,len(p)+1):
#        ans[i]=0
#        for j in range(1,len(p)+1):
#            if(i!=j and i in p[j]):
#                q=(ans[j]/len(p[j]))
#                ans[i]+=q
#        prob[i]=(((1-damping_factor)/no_of_pages)+damping_factor*ans[i])
##    print("prob array is",prob)    
##    print("ans array is",ans,"\n")    
#    for i in range(1,len(p)+1):
#        if(abs(prob[i]-ans[i])<epsila):
#            condition=False  
#    ans=prob
##    print("ans array is" ,ans)
#    it+=1     
##print("PAGE RANK ALGORITHM\n",ans)
"----------------WEIGHTED AGE RANK ALGORITHM-----------------------" 

in_links=[]
out_links=[]
m_w_in=[[0 for i in range(no_of_pages)] for j in range(no_of_pages)] 
m_w_out=[[0 for i in range(no_of_pages)] for j in range(no_of_pages)] 
s_in_links=0
s_out_links=0
mo_page_rank=[]
ratio=0
for i in range(0,no_of_pages):
    in_links.append(0)
    out_links.append(0)
    mo_page_rank.append(0)
    
for i in range(1,no_of_pages):
    for j in range(len(p[i])):
        in_links[p[i][j]]+=1
    
for i in range(1,no_of_pages):
    out_links[i]=len(p[i])
        
for i in range(1,no_of_pages):
    for j in range(1,no_of_pages):
        if(i!=j):
            for l in range(len(q[i])):
                s_in_links+=in_links[q[i][l]]
            ratio=1.0*in_links[j]/s_in_links
        else:
            pass
        m_w_in[i][j]=ratio
        s_in_links=0

for i in range(1,no_of_pages):
    for j in range(1,no_of_pages):
        if(i!=j):
            for l in range(len(q[i])):
                s_out_links+=out_links[q[i][l]]
            ratio=1.0*out_links[j]/s_out_links
        else:
            pass
        m_w_out[i][j]=ratio
        s_out_links=0

"---------------DAMPING FACTOR----------------"
pr=[1.0/(no_of_pages-1) for i in range(0,no_of_pages+1)]
for _ in range(10):
    for i in range(1,no_of_pages):
        index_sum=0
        for j in q[i]:
            index_sum+=pr[j]*m_w_in[j][i]*m_w_out[j][i]
        pr[i]=(1-damping_factor)+damping_factor*(index_sum)
print(pr)
#for i in range(1,no_of_pages):
#    index_sum=0
#    for j in range(1,no_of_pages):
#        for k in range(1,len(p[j])):
#            if(p[j][k]==i):
#                
#                ''' ye pkka nhi h ki p use krna h shyd p_sec bhi use kr ste h'''
#                index_sum+=m_w_in[j][i]*m_w_out[j][i]*ans[j]
#                
#    mo_page_rank[i]=((1-damping_factor)+damping_factor*index_sum)
    
#print(p)
#print(p_sec)
#print(in_links)
#print(out_links)
#print(m_w_in)  
#print(m_w_out)
#print(mo_page_rank)    
"--------------------HITS ALGORITHM-----------------------"
#auth={}
#hub={}
#
#for i in range(1,no_of_pages):
#    auth[i]=1
#    hub[i]=1
#for i in range(10):
#    norm=0
#    for j in range(1,no_of_pages):
#        auth[j]=0
#        for m in q[j]:
#            auth[j]=auth[j]+hub[m]
#        norm+=pow(auth[j],2) 
#    norm=math.sqrt(norm)
#    for i in range(1,no_of_pages):
#        auth[i]=auth[i]/norm
#    norm=0
#    for j in range(1,no_of_pages):
#        hub[i]=0
#        for m in p[j]:
#            hub[j]+=auth[m]
#        norm+=pow(hub[j],2)
#    norm=math.sqrt(norm)
#    for i in range(1,no_of_pages):
#        hub[i]=hub[i]/norm
#
#for i in range(1,no_of_pages):
#    print(hub[i],)
#print("")
#for i in range(1,no_of_pages):
#    print(auth[i])    
#            
    
