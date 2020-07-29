
import random
from pprint import pprint
j=0
p={1:[],
   2:[1,3],
   3:[1,4],
   4:[1,2]}
#for i in range(1,5):
#    p[i]=[]
#for i in range(1,5):
#    random_no=random.randint(1,4)
#    while j<random_no:
#        b=random.randint(1,4)
#        if (i!=j and (b not in p[i]) ):
#            p[i].append(b)
#        j+=1
#    j=0
    
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
'''-----------------------TO FIND PROBABILITY-----------------'''
iterations=1
flag=1
probability=[]
for i in range(0,5):
    probability.append(1/4)
print(probability)    
for i in range(0,iterations):
    if flag==0:
        break
    for j in range(1,5):
        probability[j]=(((1-damping_factor)/4)+damping_factor*ans[j])
    print("PROBABILITY",probability)
    print("ANS",ans)    
    for j in range(1,5):    
        print(abs(probability[j]-ans[j]))    
#       
#'''---adjacency matrix-----'''
#a_matrix=[0,0,0,0,0]  
#l=0
#for q in range(1,5):
#    index=0
#    temp=[]   
#    for w in range(1,4):
#        if(p[q][index] == w):
#            temp.append(1)
#        else:
#            temp.append(0)
#        index+=1    
#    a_matrix[l]=temp
#    l+=1
#print(a_matrix)    
                    
            

