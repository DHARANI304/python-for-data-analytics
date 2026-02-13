# checking the lambda which working as doubler or triple
def fun(n):
    return lambda x:x*n
res = fun(3)
print(res(5))

#write a function which takes a input from the user and print a table

def table (n):
    return lambda x:x*n

n= int(input("enter a number to print a table"))
table_cal = table(n)
for i in range(1,11):
    print(table_cal(i))


#write a lines of code to print afactorial of a number don't use buitin functions[IMP]

def factorial(n):
    if n==1:
        return 1
    else:
        return(n*factorial(n-1))
n=int(input("enter a number for the factorial"))
res = factorial(n)
print(res)# factorial fun is calling itself again and again is called recursive fun

#Take 2 input from the console "hello""world" and concat it
a= input("enter a word from user")
b= input("enter another word from user")
res=a+b
print(res)

#using a TURTLE MODULE to create a angle
import turtle
piggy=turtle.Turtle()
def polygon(l,n):
    angle = 360/n
    for i in range(n):
        piggy.fd(l)
        piggy.lt(angle)
polygon(150,6)
res=input("enter a lenght", )
print(res)

#LIST
lst = [[1,2,3],(1,2,3),{7,8,9},{1:'a',2:'b'}]
print(lst[1][0])
print(lst[2].pop())
