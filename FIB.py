# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
import math 
import time


def fib(num):
    if(num<=2):
        return 1
    else:
        return fib(num-1)+fib(num-2)

def forfib(num):
    a = 0
    b = 1
    for x in range(num):
        c = a + b
        b = a
        a = c
    return c

def tailfib(num, a, b):
    if(num==1):
        return a+b
    else:
        c = a+b
        b=a
        a=c
        return tailfib(num-1, a, b)
        
def closedfib(num):
    a = (math.sqrt(1/5)*((((1+math.sqrt(5)) /2)**num )-(((1-math.sqrt(5)) /2)**num )))
    return int(a)
    
start = time.time()    
print(fib(40))
end = time.time()
print(end - start)
start = time.time()
print(forfib(40))
end = time.time()
print(end - start)
start = time.time()
print(tailfib(40, 0, 1))
end = time.time()
print(end - start)
start = time.time()
print(closedfib(40))
end = time.time()
print(end - start)
#354224848179261915075
