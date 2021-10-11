# for loop with else


a=[1,2,3,4,5]

for item in a:
    print(item)
    if(item==3):
        break
else:
    print("we are inside else")
print("we have finished the loop")

for item in a:
    
    if(item==3):
        continue
    print(item)
else:
    print("we are inside else")
print("we have finished the loop")

