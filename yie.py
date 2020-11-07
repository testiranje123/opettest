def par(num):
    for i in range(1,num):
        if i%2==0:
            yield i

c=0
for j in par(50):
    print (j)