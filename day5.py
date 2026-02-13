# math operations
import math
print(math.sqrt(16))
print(math.factorial(5))
print(math.floor(3.7))
print(math.ceil(3.2))
print(math.pow(2, 3))
print(math.pi)
print(math.e)

#LAMBDA PTRHON FUNCTIONS(IMP)
res = (lambda num,power:num**power)(5,2)
print(res)
# Addition lamda function
res =(lambda a,b:a+b)
print(res(10,20))
print(res(100,200))
# Adding using the console
print("enter a number")
a=int(input())
print("enter the anthor number")
b=int(input())
res=(lambda a,b:a+b)(a,b)
print(res)

#using FILTER FUNCTION WITH LAMBDA
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)

#using MAP FUNCTION WITH lambda
numbers = [1,2,3,4,5,6,7,8,9,10]
square_number = list(map(lambda x: (x**2), numbers))
print("square_number", square_number)

#using REDUCE FUNCTION with def
lst = [1,2,3,4,5,6,7,8,9,10]
def red_lst(lst):
    sum=0
    for i in lst:
        sum=sum+i
    return sum;
res = red_lst(lst)
print(res)
#using REDUCE FUNCTION WITH lambda
from functools import reduce
numbers = [1,2,3,4,5,6,7,8,9,10]
sum_of_numbers=list(reduce(lambda x,y : x+y, numbers))
print("sum of numbers",sum_of_numbers)




 
 


