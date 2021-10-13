# functions with arguments

def average(a,b,c):
    return(a+b+c)/3

avg=average(3,6,4)
print(avg)

# function with default arguments

def greet(name="priya"):
    return "hello "+name
# a=greet("sivaa")
a=greet()
print(a)

# recursions

def factorial(n):
    if(n==0 or n==1):
        return 1
    return n*factorial(n-1)
a=factorial(5)
print(a)