# access each and every element of a list using for loop
lst = [1,2,3,4,5,6,7,8,9,10]
for i in lst:
    print(i)

#access each and every element of a list and also with the index value
lst = [1,2,3,4,5,6,7,8,9,10]
for i in range(len(lst)):
    print("index value",i,"element value",lst[i])
#USING ENUMERATE FUNCTION
lst = [1,2,3,4,5,6,7,8,9,10]
for index, value in enumerate(lst):
    print("index value", index, "element value", value)
#For nested list using enumerate function
lst = [[1,2], [3,4], [5,6]]
for index, sublist in enumerate(lst):
    print("index value", index, "sublist", sublist)
#access each and every element of a list and also with the index value
lst = [[1,2], [3,4], [5,6]]
for i in lst:
    for j in i:
        print(j)
#reversing of a list
a = [1,2,3,4,5,6,7,8,9,10]
rev = a[::-1]
print(rev)

#sorting of a list
a=[10,20,70,60,50,30]
res = sorted(a)
print(res)
res1= sorted(a,reverse=True)
print(res1)

#Membership check:
a = [10,20,30,40.50]
print(20 in a)


