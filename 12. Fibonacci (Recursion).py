#1st method:

x = int(input("Enter any integer: "))

def fib(x):
    """assumes x an int >= 0
       returns Fibonacci of x"""
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-1) + fib(x-2)

print(fib(x))

########################################################################################################################

#2nd method:

x = int(input("Enter any integer: "))
def fib(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    else:
        return fib(x-1) + fib(x-2)
print(fib(x))

########################################################################################################################

#3rd and most effiecient method using dictionary

x = int(input("Enter any integer: "))

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d)+fib_efficient(n-2, d)
        d[n] = ans
        return ans
        
d = {1:1, 2:2}

print(fib_efficient(x, d))

