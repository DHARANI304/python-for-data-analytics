#set comparision
s1 = {1,2,3,4}
s2 = {3,4,5,6}
print(s1|s2) # GIVES output which is unique in the both tables
print(s1.union(s2))
print(s1&s2)
print(s1.intersection(s2))
print(s1.difference(s2))# checks and give soutput only from the one table
print(s1^s2)# when i want unique vLUES FROM both tables
# ADD,REMOVE AND DISCARD AN EMENT
s = {1,2,3,4,5}
s.add(6)
print(s)
s.remove(2)
print(s)
s.discard(3)
print(s)

