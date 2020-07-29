f=open("links-simple-sorted.txt","r")
p={}
no_of_pages=1000
mod_val=100
d_new_calc=0
d_calc=0
for i in range(1,no_of_pages):
    data=f.readline()
    data_list=data.split(': ')
    data_list_1=int(data_list[0])
    data_list_2=data_list[1].split(' ')
#    print(data_list_1,data_list_2)
    p[data_list_1]=data_list_2
    if '\n' in p[data_list_1][-1]:
        p[data_list_1][-1]=p[data_list_1][-1][:-1]
sorted(p.keys())        
for i in p.keys():
    for j in range(len(p[i])):
        p[i][j]=int(p[i][j]) % mod_val
print(p)        
    