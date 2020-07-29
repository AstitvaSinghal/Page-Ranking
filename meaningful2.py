f=open("quotes.txt",'r')
nf=open("meaningful_words.txt",'w')
c=0
visited={}
while(1):
    s=f.readline()
    if(not s):
        break
    words=s.split()
    words=[i.lower() for i in words]
    for i in words:
        ch=""
        for j in i:
            if((j>='a' and j<='z') or (j>='A' and j<='Z')):
                ch+=j
        
        c+=1
        try:
            if(visited[ch]==1):
                continue
        except KeyError:
            nf.write(ch+'\n')
            visited[ch]=1
            print ch
