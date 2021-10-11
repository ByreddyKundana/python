# chapter 7 practice set


# program to print a multiplication table of a number using 
# for loop

num=int(input("enter the number: "))

for i in range(1,11): 
    # print(num,"*",i,"=",num*i)
    print(f"{num}*{i}={num*i}")

# program to greet people in list
li=["shiv","rani","vani","raj"]

for item in li:
    print(f"good morning {item}")

# program to find prime number

num=int(input("enter the number: "))

for i in range(2,num):
    if(num%i==0):
        print("not prime")
        break
else:
    print("the number is prime")

# sum of firwst n natural  num using while loop

i=1
sum=0
n=int(input("enter the range: "))
while(i<=n):
    sum+=i
    i+=1
print(f"the sum of first {n} natural numbers is {sum}")


#pyramid pattern
n=int(input("enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1-i):
        print(" ",end="")
        j+=1
    for k in range(2*i-1):
        print("*",end="")
        k+=1
    print("\n",end="")
    i+=1

    


