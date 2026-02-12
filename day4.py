#ARGUMENTS
# POSITIONAL ARGUMENTS
def power_off(num,power):
    print(num**power)
power_off(2,5)
power_off(5,2)

# KEYWORD ARGUMENTS
def power_off(num,power):
    print(num**power)
power_off(power=2,num=5)
power_off(num=5,power=2)

# DEFAULT ARGUMENTS
def power_off(num,power=2):
    print(num**power)
power_off(5)
power_off(2,5)
power_off(3,5)

# VARIABLE LENGTH ARGUMENTS
def submit_details(*details):
    print(details)
submit_details("sana",25,"INDIA")
submit_details("Dharani",30,"Engineer")

#TAKING INPUT FROM USER
print("enter a number")
a = input()
print("enter another number")
b = input()
def add(a, b):
    c = int(a) + int(b)
    return c
result = add(a, b)
print(result)

#write a lines of code from the console and print to the moniter
print("Enter the line of the code")
code = input()
exec(code)

#write a programs where it takes input from the user and check if it ia even or odd
print("enter a number")
num= int(input())
if (num%2==0):
    print("even")
else:
    print("odd")

# write a program that takes input from the user and print if it is a vowel or consonant
print("Enter a character")
char= input()
if char in('a','e','i','o','u','A','E','I','O','U'):
    print("vowel")
else:
    print("consonant")

#another version
print("Enter a Alphabet")
char= input()
char.islower()
if char in('a','e','i','o','u'):
    print("vowel")
elif char in('A','E','I','O','U'):
    print("vowel")
else:
    print("consonant")

# write a program takes input from the user and check if he is eligible for voting or not
print("Enter age")
age=int(input())
if age>=18:
    print("eligible for voting ")
else:
    print("not eligible for voting")

#write a progem that takes input from the user and check if the year is leap year or not
print("Enter year")
year=int(input())
if(year%4==0 and year%100!=0) or (year%400==0):
    print("leap year")
else:
    print("not a leap year")

#write a program if the number is divisible by 3 and 7
print("Enter a number")
num= int(input())
if(num%3==0):
    print("divisible by 3")
elif(num%7==0):
    print("divisible by 7")
else:
    print("number is not divisible by 3 and 7")

