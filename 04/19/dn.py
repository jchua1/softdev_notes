a = []

for i in range(10):
    a.append(i ** 2)

print a

b = [x for x in range(10)]
print b

c = [x**2 for x in range(10)]
print c

d = [(x, x*x, x*x*x) for x in range(10)]
print d

string = 'nooberry'
e = [string[x] for x in range(len(string))]
print e

f = [x for x in string]
print f

aString = 'aaaabbbbccccdddd'
fav = 'b'
g = [x for x in aString if x == fav]
print g

first = 'nooberry'
second = 'uber'
h = [x for x in first if x in second]
print h

i = [x if x in second else 0 for x in first]
print i 
