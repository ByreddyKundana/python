# chapter 5 practice set

# dictionary with hindi words with values as their english translation
oxford={
    "lakdi":"wood",
    "kursi":"chair",
    "chaku":"knife"
}
key=input("enter the key\n")
if(oxford.get(key)==None): 
   print("value not found")   
else: 
 print("the value corresponding to your key is: ",oxford.get(key))

# program to input 8 numbers from user and display all the unique numbers

s=set()
for i in range(8):
    s.add(int(input("enter the number: ")))
print(s)
