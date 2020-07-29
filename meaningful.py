f=open("quotes.txt",'r')
nf=open("meaningful_words.txt",'w')
s=f.readline()
visited={}
while(s):
    s=s.split()
    for i in s:
        try:
            print visited[i]
            if(visited[i]==1):
                continue
        except KeyError:
            visited[i]=1
        print i
        n=raw_input()
        if(n=='y'):
            nf.write(i+'\n')
        elif(n=='n'):
            continue
        elif(n==','):
            try:
                if(visited[i[0:-1]]==1):
                    continue
            except KeyError:
                visited[i[0:-1]]=1
            nf.write(i[0:-1]+'\n')
        else:
            nf.write(n+'\n')
    s=f.readline()
            

f.close()
