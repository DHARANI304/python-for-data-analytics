# SHALLOW COPY
a = [1,2,3,4,5]
b = a[:]
print(id(a))
print(id(b))
b.append(99)
print(b)
print(a)

a = [[1,2], [3,4]]
b= a[:]
print(id(a))
print(id(b))
b.append([5,6])
b[0][1] = 44
print(b)

#LIST COMPRAHENSION(IMP)
# Write a lines of code to do each element of list = [1,2,3,4]
lst =[1,2,3,4]
cube_of_numbers = []
for i in lst:
    cube_of_numbers=(i**3)
print(cube_of_numbers)

#in a single line
lst=[1,2,3,4]
cube_numbers = [i**3 for i in lst]
print(cube_numbers)

# check wheather its a evaen numbers or odd numbers
a = [1,2,3,4,5,6,7,8,9,10]
b =[]
odd_num=[]
for num in a:
    if(num%2==0):
        b.append(num)
        print("even numbers" )
    else:
        print("odd numbers")
        odd_num.append(num)
print(b)
print(odd_num)

#in a single line
a=[1,2,3,4,5,6,7,8,9,10]
even_num=[i%2==0 for i in a]
print(even_num)

lst=[1,2,3,4,5,6,7,8,9,10]
even_num =[]
odd_num =[]
for i in lst:
    if(i%2==0):
        even_num.append(i**2)
    else:
        odd_num.append(i**3)
print(even_num)
print(odd_num)

#doing in a list conversion

a=[1,2,3,4,5,6,7,8,9,10]
even_odd_num=[i**2 if i%2==0 else i**3 for i in a]
print(even_odd_num)


