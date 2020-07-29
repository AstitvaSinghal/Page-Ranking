import random
from pprint import pprint
"----------------------RANDOM GRAPH-------------"
no_of_pages=100
p={}
p_sec={}
j=0
for i in range(1,no_of_pages):
    p[i]=[]
    p_sec[i]=[]
for i in range(1,no_of_pages):
    random_no=random.randint(1,no_of_pages-1)
    while j<random_no:
        b=random.randint(1,no_of_pages-1)
        if (i!=b and (b not in p[i]) ):
            p[i].append(b)
            p_sec[b].append(i)
        j+=1
    j=0
"-----------------------------------------------------"
"------------------ PAGE RANK ALGORITHM---------------------------"    
page_rank=0.25
damping_factor=0.85
ans=[]
prob=[]
epsila=random.uniform(0,0.0005)
condition=True;
it=0
for i in range(0,len(p)+1):
    ans.append(0.25)
    prob.append(0)
while(condition):
#    print(epsila)
#    print("Iteration",it)
    for i in range(1,len(p)+1):
        ans[i]=0
        for j in range(1,len(p)+1):
            if(i!=j and i in p[j]):
                q=(ans[j]/len(p[j]))
                ans[i]+=q
        prob[i]=(((1-damping_factor)/no_of_pages)+damping_factor*ans[i])
#    print("prob array is",prob)    
#    print("ans array is",ans,"\n")    
    for i in range(1,len(p)+1):
        if(abs(prob[i]-ans[i])<epsila):
            condition=False  
    ans=prob
#    print("ans array is" ,ans)
    it+=1     
                   
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
    in_links[i]=len(p_sec[i])
    
for i in range(1,no_of_pages):
    out_links[i]=len(p[i])
        
for i in range(1,no_of_pages):
    for j in range(1,no_of_pages):
        if(i!=j):
            for l in range(len(p[i])):
                s_in_links+=in_links[p[i][l]]
            ratio=in_links[j]/s_in_links
        else:
            pass
        m_w_in[i][j]=ratio
        s_in_links=0

for i in range(1,no_of_pages):
    for j in range(1,no_of_pages):
        if(i!=j):
            for l in range(len(p[i])):
                s_out_links+=out_links[p[i][l]]
            ratio=out_links[j]/s_out_links
        else:
            pass
        m_w_out[i][j]=ratio
        s_out_links=0

"---------------DAMPING FACTOR----------------"
for i in range(1,no_of_pages):
    index_sum=0
    for j in range(1,no_of_pages):
        for k in range(1,len(p[j])):
            if(p[j][k]==i):    
                ''' ye pkka nhi h ki p use krna h shyd p_sec bhi use kr ste h'''
                index_sum+=m_w_in[j][i]*m_w_out[j][i]*ans[j]
                
    mo_page_rank[i]=((1-damping_factor)+damping_factor*index_sum)
    
#print(p)
#print(p_sec)
#print(in_links)
#print(out_links)
print(m_w_in)  
print(m_w_out)
print(mo_page_rank)   
print(sum(mo_page_rank)) 