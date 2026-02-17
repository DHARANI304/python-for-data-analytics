s = {1,2,3,4,5,6}
s1 =set()
for i in s:
    s1.add(i**2)
print(s1)
#If a numbers is odd then print cube if it is even print square
s = {1,2,3,4,5,6,7,8,9,10}
s1 = set()
for i in s:
    if(i%2==0):
        b=i**2
        s1.add(b)
    else:
        c=i**3
        s1.add(c)
print(s1)

S1 = {i**2 if i%2==0 else i**3 for i in s}
print(S1)

s1 = {1,2,3,4,5,6}
s2 = {3,4,5,7,8,9}
s = set()
s3 = set()
for i in s1:
    for j in s2:
        s = s1.intersection(s2)
        for i in s:
            b=i**2
            s3.add(b)
print(s)
print(s3)