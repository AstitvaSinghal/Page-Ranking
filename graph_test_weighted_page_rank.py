
import random
from pprint import pprint
no_of_pages=5
"------------DECIDED GRAPH-----------------"
#p={1:[2,3],
#   2:[1,3],
#   3:[1],
#   4:[1,2,3],}
"-------------------------------------------"
"-----------------RANDOM GRAPH---------------"
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
'''--------------------------------------------'''    
page_rank=0.25
cols=5
rows=5
damping_factor=0.85
lis_of_w_in=[]
lis_of_w_out=[]
matrix_of_w_in=[]
matrix_of_w_out=[]
sum_of_in_links=0
sum_of_out_links=0
a=0
"---------------PAGE RANK ORIGINAL---------------"
ans=[]
probability=[]
for i in range(0,len(p)+1):
    ans.append(0)
for i in range(1,len(p)+1):
    for j in range(1,len(p)+1):
        if(i!=j and i in p[j]):
            q=(page_rank/len(p[j]))
            ans[i]+=q
for i in range(0,5):
    probability.append(1/(no_of_pages-1))            
for j in range(1,5):
    probability[j]=(((1-damping_factor)/4)+damping_factor*ans[j])            
"----------------PAGE RANK MODIFIED-----------------------"            
for i in range(0,no_of_pages):
    lis_of_w_in.append(0)
    lis_of_w_out.append(0)

matrix_of_w_in=[[0 for i in range(cols)] for j in range(rows)] 
matrix_of_w_out=[[0 for i in range(cols)] for j in range(rows)] 
for i in range(1,no_of_pages):
    for j in range(len(p[i])):
        lis_of_w_in[p[i][j]]+=1

for i in range(1,no_of_pages):
    lis_of_w_out[i]=len(p[i])            
for i in range(1,no_of_pages):
    for j in range(1,no_of_pages):
        if(i!=j):
            for l in range(len(p[i])):
                sum_of_in_links+=lis_of_w_in[p[i][l]]    
           # print("i is",i,"j is",j,p[i],"j value is",lis_of_w_in[j] ,sum_of_in_links)    
            a=round((lis_of_w_in[j]/sum_of_in_links),3) 
        else:
            pass
        matrix_of_w_in[i][j]=a 
        #pprint(matrix_of_w_in)
        sum_of_in_links=0
        a=0
for i in range(1,no_of_pages):
    for j in range(1,no_of_pages):
        if(i!=j):
            for l in range(len(p[i])):
                sum_of_out_links+=lis_of_w_out[p[i][l]]
            a=round((lis_of_w_out[j]/sum_of_out_links),3)
        else:
            pass
        matrix_of_w_out[i][j]=a 
        sum_of_out_links=0
        a=0
print("p is")
pprint(p)
print("ans is")
print(ans)
print("lis_of_w_in",lis_of_w_in,"\n")  
print("lis_of_w_out",lis_of_w_out,"\n")
pprint(matrix_of_w_in)  
print("\n")
pprint(matrix_of_w_out) 


"-----------------DAMPING FACTOR--------------"

modified_page_rank=[0,0,0,0,0]
for i in range(1,no_of_pages):
    sum_of_index=0
    for j in range(1,no_of_pages):
        for k in range(len(p[j])):
            if(p[j][k]==i):
                sum_of_index+=matrix_of_w_in[j][i]*matrix_of_w_out[j][i]*ans[j]
                r=matrix_of_w_in[j][i]*matrix_of_w_out[j][i]*ans[j]
               # print("i is",i,"j is",j,"k is",k,"matrix_of_w_in",matrix_of_w_in[j][i],"matrix_of_w_out",matrix_of_w_out[j][i],"ans",ans[j],"r",r,"sum_of_index",sum_of_index)  
    modified_page_rank[i]=round(((1-damping_factor)+damping_factor*(sum_of_index)),4)
   # print(sum_of_index)
    #print("\n")


print(modified_page_rank)    