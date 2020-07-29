a={1:[1,2,3,4,5,6,7,8,9],2:[1,2,3,4,5]}
for i in range(0,5):
    b=random.randint(1,15)
    print("b value",b)
    if(b not in a[1]):
        print("inside b value",b)
        a[1].append(b)
print(a)        