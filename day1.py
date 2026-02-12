a1=(10,20,30)
b1={10,10.5,"Dharani",20}
print(a1)
print(b1)
c=b1.add("Hello")
print(c)

keys = ["name", "age", "course"]
values = ["Dharani", 21, "Python"]

student = dict(zip(keys, values))
print(student)

# day 3
# INPUT WITH NO OUTPUT FUN
def add(a, b):
    c=a + b
    print(c)
x=10
y=20
add(x, y)
