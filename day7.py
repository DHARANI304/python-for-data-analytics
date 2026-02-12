# list slicing
lst=[1,2,3,4,5,6,7,8,9,10]
print(lst[2:7])# here it will take the index value where 2 is inclusive and 7 is exclusive
print(lst[1:])# if we want to print till last we can only give inclusive number
print(lst[ :3])
print(lst[1::2])

#Adding element to the the list
#add list to the existing list
#delete a portion of the list 
lst = [1,2,3,0,4]
lst.insert(3, 33)  # Insert 33 at index 3
print(lst)
lst.extend([5,6,7])  # Extend the list with another list
print(lst)
lst = [1,2,3,4,5,6,7,8,9,10]
del lst[6:9]  # Delete elements from index 6 to 8 (exclusive)
print(lst)
# Remove the numbers from the list
# remove last element from the list
#remove 0 index element from the list
# Add multiple elements in  the middle of the list
lst = [10,20,30,40]
del lst[2:]
print(lst)
lst.pop()  # Remove the last element
print(lst)
lst.pop(0)  # Remove the element at index 0
print(lst)
lst = [1,2,3,8,9,10]
new_elements = [4,5,6,7]
brk_point = 3
lst2 = lst[:brk_point] + new_elements + lst[brk_point:]
print(lst2)
#replicate  a list 10 times
lst = [1,2,3]
replicate_lst = lst*10
print(replicate_lst)
# copy a list where id should be different
lst = [1,2,3]
copy_lst = lst.copy()
print(copy_lst)
print(id(lst))
print(id(copy_lst))
d = lst[:]
print(d)
print(id(d))



