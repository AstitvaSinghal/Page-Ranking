import pprint
f=open("quotes.txt","rt")
quotes=[]
text=(f.readline())[0:-1]
quotes.append(text)
words=text.split()
wordDict={}
skipWords=['to', 'what', 'my', 'a', 'that', 'and', 'who', 'The', 'are', 'is', 'it', 'in', 'I', 'It', 'the', 'be', 'on', 'of', 'your', 'you']

#reads quote from file, extracts words and add them to a dictionary with value as a list of quotes that contain that word
while(text):
    for i in words:
        if(i in skipWords):
            continue
        try:
            wordDict[i].append(text)
        except KeyError:
            wordDict[i]=[text]
    text=(f.readline())[0:-1]
    if(text==''):
        break
    quotes.append(text)
    words=text.split()

#it makes a dictionary that tells quotes with the same words with the given quote
similarQuote={}
for i in quotes:
    wordsInQuote=i.split()
    for j in wordsInQuote:
        if(j in skipWords):
            continue
        try:
            l=similarQuote[i]+wordDict[j]
            for k in range(l.count(i)):
                l.remove(i)
            
            similarQuote[i]=l
        except KeyError:
            l=[]+wordDict[j]
            for k in range(l.count(i)):
                l.remove(i)
            similarQuote[i]=l
    similarQuote[i].sort()
similar={}
for i in quotes:
    #print i,
    similarQuote[i].sort()
    j=0
    while(j<len(similarQuote[i])):
        n=similarQuote[i].count(similarQuote[i][j])
        print n,
        if(n>=2):
            try:
                similar[i].append(similarQuote[i][j])
            except KeyError:
                similar[i]=[similarQuote[i][j]]
        j=j+n
    print '\n'
pprint.pprint(similar)
#print search