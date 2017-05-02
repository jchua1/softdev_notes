import time

def name_args(f):
    def log(*arg):
        #print 'Function Name: ' + f.func_name
        #print 'Arguments: ' + str(arg)
        print f.func_name + ': ' + str(arg)
        return f(*arg)
    return log

def exec_time(f):
    def log(*arg):
        start = time.time()
        ret = f(*arg)
        end = time.time()
        t = end - start
        print 'execution time: ' + str(t)
        return ret
    return log

#@exec_time
#@name_args
#def fib(x):
#    if x < 2:
#        return 1
#    else:
#        return fib(x-1) + fib(x-2)

#print fib(6)

fibcache = {}
def fib(n):
    if n in fibcache:
        return fibcache[n]
    else:
        fibcache[n] = n if n < 2 else fib(n-1) + fib(n-2)
        return fibcache[n]

print fib(7)
#print fibcache

def cache(f):
    fcache = {}
    def run(n):
        if n not in fcache:
            fcache[n] = f(n)
        return fcache[n]
    return run

@cache
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) + fib(n-2)

print fib(7)
