# chapter 6 practice set
a=45
b=6
c=86
d=23

if(a>b):
    maxNum1=a
else:
    maxNum1=b
if(c>d):
    maxNum2=c
else:
    maxNum2=d
if(maxNum2>maxNum1):
    maxNum=maxNum2
else:
    maxNum=maxNum1
print("maximum number out of these four numbers is: ",maxNum)

# determining whether a student is pass or fail

m1=int(input("enter marks for sub 1: "))
m2=int(input("enter marks for sub 2: "))
m3=int(input("enter marks for sub 3: "))

overAll=(m1+m2+m3)/3

if(overAll>=40):
    if(m1>=33 and m2>=33 and m3>=33):
        print("you have passed the exam")
    else:
        print("you have not passed the exam due to one of the sub")
else:            
 print("you have not passed the exam")


# 3 rd question

spamWords=['buy now','subscribe this','click this']
# email='this is a new stock.You need to click this and buy this stock'
email=input("enter your email: ").lower()
spam=False
if('buy now'in email):
    spam=True
if('subscribe this'in email):
    spam=True
if('click this'in email):
    spam=True

print("spam is",spam)

