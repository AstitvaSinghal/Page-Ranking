import pprint
import math
import random

f=open("meaningful_words.txt",'r')
l={}
while(1):
    s=f.readline()
    if(not s):
        break
    s=s.lower()
    ch=""
    for j in s:
        if((j>='a' and j<='z') or (j>='A' and j<='Z')):
            ch+=j
    l[ch]=1
    
f.close()

def distinctList(l):
    nl=[]+l
    nl.sort()
    i=0
    sl=[]
    while(1):
        if(i>=len(nl)):
            break
        c=nl.count(nl[i])
        sl.append(nl[i])
        i=i+c
    return sl
        


f=open("quotes.txt",'r')
word_count={}
quote_for_word={}
while(1):
    s=f.readline()
    if(not s):
        break
    s=s.lower()
    words=s.split()
    for i in words:
        ch=""
        for j in i:
            if((j>='a' and j<='z') or (j>='A' and j<='Z')):
                ch+=j
        try:
            if(l[ch]==1):
                try:
                    if(s not in quote_for_word[ch]):
                        quote_for_word[ch].append(s)
                except KeyError:
                    quote_for_word[ch]=[s]
                try:
                    word_count[s]+=1
                except KeyError:
                    word_count[s]=1
        except KeyError:
            continue
f.close()
f=open("quotes.txt",'r')
similarMap={}
while(1):
    s=f.readline()
    if(not s):
        break
    s=s.lower()
    cluster=[]
    words=s.split()
    for i in words:
        ch=""
        for j in i:
            if((j>='a' and j<='z') or (j>='A' and j<='Z')):
                ch+=j
        try:
            if(l[ch]==1):
                cluster+=quote_for_word[ch]
        except KeyError:
            continue
    
    cluster=distinctList(cluster)
    if(len(cluster)==1):
        cluster.append(word_count.keys()[random.randint(0,len(word_count.keys())-1)])
        print cluster
    
    clusterMap=[]
    for i in cluster:
        clusterMap.append({"quote":i,"count":word_count[i]})
    clusterMap.sort(key=lambda x: x["count"])
    clusterMap.reverse()
    if(len(clusterMap)>2):
        clusterMap=clusterMap[0:random.randint(2,len(clusterMap)-1)]
    ast=[i["quote"] for i in  clusterMap]
    #print clusterMap,"\n",ast,"\n*******\n"
    similarMap[s]=ast
#for i in similarMap.keys():
#    print len(similarMap[i])
#    if(len(similarMap[i])==0):
#        print i
ptoq={}
qtop={}

for i in range(1,len(similarMap.keys())+1):
    qtop[similarMap.keys()[i-1]]=i
    ptoq[i]=similarMap.keys()[i-1]
p={}
q={}
for i in similarMap.keys():
    q[qtop[i]]=[]
for i in similarMap.keys():
    p[qtop[i]]=[]
    for j in similarMap[i]:
        if(qtop[i]==qtop[j]):
            continue
        p[qtop[i]].append(qtop[j])
        try:
            q[qtop[j]].append(qtop[i])
        except KeyError:
            q[qtop[j]]=[qtop[i]]
#print p
#print q

#adj=[[0 for i in range(len(similarMap.keys()))] for j in range(len(similarMap.keys()))]
#for i in similarMap.keys():
#    out=similarMap[i]
#    for j in out:
#        adj[qtop[i]-1][qtop[j]-1]=1
#    print adj[qtop[i]-1]
no_of_pages=len(similarMap.keys())

#----Power Rank ------ #
t=0
beta=0.5
gamma=0.5

P=[]
PN=[]
for i in range(0,no_of_pages+1):
    P.append(0)
    PN.append(0)

while(t<30):
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
#print PN

pageRank=[]
for i in range(1,len(PN)):
    pageRank.append({"page":i,"rank":PN[i]})
pageRank.sort(key=lambda x:x["rank"])
pageRank.reverse()
top=[i["page"] for i in pageRank]
print "Power Rank",top[0:10]


"----------------WEIGHTED AGE RANK ALGORITHM-----------------------" 
damping_factor=0.85
in_links=[]
out_links=[]
m_w_in=[[0 for i in range(no_of_pages+1)] for j in range(no_of_pages+1)] 
m_w_out=[[0 for i in range(no_of_pages+1)] for j in range(no_of_pages+1)] 
s_in_links=1
s_out_links=1
mo_page_rank=[]
ratio=0
for i in range(0,no_of_pages+1):
    in_links.append(0)
    out_links.append(0)
    mo_page_rank.append(0)
    
for i in range(1,no_of_pages+1):
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
        s_in_links=1

for i in range(1,no_of_pages):
    for j in range(1,no_of_pages):
        if(i!=j):
            for l in range(len(q[i])):
                s_out_links+=out_links[q[i][l]]
            ratio=1.0*out_links[j]/s_out_links
        else:
            pass
        m_w_out[i][j]=ratio
        s_out_links=1

"---------------DAMPING FACTOR----------------"
pr=[1.0/(no_of_pages-1) for i in range(0,no_of_pages+1)]
for _ in range(10):
    for i in range(1,no_of_pages):
        index_sum=0
        for j in q[i]:
            index_sum+=pr[j]*m_w_in[j][i]*m_w_out[j][i]
        pr[i]=(1-damping_factor)+damping_factor*(index_sum)
#print(pr)
pageRank=[]
for i in range(1,len(pr)):
    pageRank.append({"page":i,"rank":pr[i]})
pageRank.sort(key=lambda x:x["rank"])
pageRank.reverse()
top=[i["page"] for i in pageRank]
print "Weighted Page rank",top[0:10]
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
#print("Answer=",ans," and sum= ",sum(ans)-0.25)  

pageRank=[]
for i in range(1,len(ans)):
    pageRank.append({"page":i,"rank":ans[i]})
pageRank.sort(key=lambda x:x["rank"])
pageRank.reverse()
top=[i["page"] for i in pageRank]
print "Page ranking",top[0:10]


"-------------------------Algorithm---------------"

auth={}
hub={}

for i in range(0,no_of_pages+1):
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

#for i in range(1,no_of_pages):
#    print(hub[i],)
#print("")
#for i in range(1,no_of_pages):
#    print(auth[i])    
pageRank=[]
auth[0]=-1
for i in auth.keys():
    pageRank.append({"page":i,"rank":auth[i]})
pageRank.sort(key=lambda x:x["rank"])
pageRank.reverse()

top=[i["page"] for i in pageRank]
print "hit ranking",top[0:10]
