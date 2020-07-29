import random
matrix_of_w_in=[]
temp=[]
for i in range(0,5):
    temp.append(random.randint(1,5))
for i in range(0,5):
    matrix_of_w_in.append(temp)
pprint(matrix_of_w_in)