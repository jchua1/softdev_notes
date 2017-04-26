import random

def inc(x):
    return x + 1

f = inc

#print f(10)

def h(x):
    return lambda y: x + y

#print h(1)
#print h(2)
#print h(1)(3)
#print h(2)(5)

b = h(1)

#print b
#print b(3)

c = h(2)

#print c
#print c(5)

def f(x):
    def g(y):
        return x + y
    return g

#print f(1)
#print f(1)(2)

def repeat(x):
    def reps(y):
        return x * y
    return reps

r1 = repeat('hello')
r2 = repeat('goodbye')

print r1(2)
print r2(2)
print repeat('cool')(3)

'''
def greeting():
    greetings = ['hi', 'hello', 'wassup', 'yo']
    return random.choice(greetings)

def farewell():
    farewells = ['bye', 'goodbye', 'cya', 'pce']
    return random.choice(farewells)

print greeting()
print farewell()
'''

def makeHTMLheading(x):
    def contents():
        return '<h1>' + x() + '</h1>'
    return contents

'''
greet_heading = makeHTMLheading(greeting)
print greet_heading()

greeting = makeHTMLheading(greeting)
print greeting()
'''

@makeHTMLheading
def greet():
    greetings = ['hi', 'hello', 'wassup', 'yo']
    return random.choice(greetings)

greet_heading = greet
print greet_heading()
