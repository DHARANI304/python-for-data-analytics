Tup =10,
Tup1 = 10,20,30,40,50
a,b,c,d,e = Tup1
print(a,b,c,d,e)
a,_,c,_,e = Tup1
print(a,c,e)

#Accessing the elements in the Tuple
a = (10,20,30,40,50)
print(a[0])
print(a[-1])

b = ((10,20), [10,20], {50,60})
print(b[0][0])

Tup =10,20,30,40,50
for i in Tup:
    print(i)
#accessing element in tuple
b=((10,20),(30,40))
for i in b:
    for j in i:
        print(j)

Tup = 10,20,30,40,50
for i in enumerate(Tup):
    print('index',i,'element',j)
for i in range(len(Tup)):
    print(i)
    print(Tup[i])

#Concatenation
a = 1,2,3
b = 4,5,6
c=a+b
print(c)

#Tuple slicing
Tup = (10,20,30,40,50,60,70,80,90,100)
b = Tup[2:6]
print(b)
c = Tup[::-1]
print(c)