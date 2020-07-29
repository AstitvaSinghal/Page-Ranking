
import random
from pprint import pprint

"----------------------RANDOM GRAPH-------------"
no_of_pages=4
p={}
j=0
for i in range(1,no_of_pages):
    p[i]=[]
for i in range(1,no_of_pages):
    random_no=random.randint(1,no_of_pages-1)
    while j<random_no:
        b=random.randint(1,no_of_pages-1)
        if (i!=j and (b not in p[i]) ):
            p[i].append(b)
        j+=1
    j=0
"-----------------------------------------------------"
"------------------ALGORITHM---------------------------"    
page_rank=0.25
damping_factor=0.85
ans=[]
for i in range(0,len(p)+1):
    ans.append(0)
for i in range(1,len(p)+1):
    for j in range(1,len(p)+1):
        if(i!=j and i in p[j]):
            q=(page_rank/len(p[j]))
            ans[i]+=q
            #print(q,i,j)
   # print("next")   

pprint(p)  
print(ans)       
'''-----------------------TO FIND PROBABILITY-----------------'''
iterations=1
flag=1
probability=[]
for i in range(0,no_of_pages):
    probability.append(1/(no_of_pages-1))
print(probability)    
for i in range(0,iterations):
    if flag==0:
        break
    for j in range(1,no_of_pages-1):
        probability[j]=(((1-damping_factor)/4)+damping_factor*ans[j])
    print("PROBABILITY",probability)
    print("ANS",ans)    
    for j in range(1,no_of_pages-1):    
        print(abs(probability[j]-ans[j]))    












        
#     '''---adjacency matrix-----'''
#    for q in range(1,5):
#        index=0
#        for w in range(1,5):
#            if(p[q][index+=1] == w):
#                temp.append('1')
#            else:
#                temp.append('0')
#        a_matrix[q].append(temp)
                    
            

