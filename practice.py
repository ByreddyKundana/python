# chapter 8 practice set
# greatest of three numbers
def greatest(num1,num2,num3):
    if(num1>num2):
        greater=num1
    else:
        greater=num2
    if(num3>greater):
        greater=num3
    return greater

a=greatest(23,27,90)
print(a)

# conversion
def ctf(cel):
    return (cel*9/5)+32
a=ctf(135)
print (a)

# prevent print () to print a new line at the end

print("priya and siva",end=" ")
print("and both")

# sun n natural num using recursion

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n
a=sum(4)
print(a)

# print pattern

def printPattern(n):
    for i in range(n):
        print("*"*(n-i))
printPattern(3)


