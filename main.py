# dictionary methods

oxford={
    "gift":"something willingly given to someone to appreciate",
    "this":"a keyword in c++",
    "youtube":"a video sharing platform",
    "instagram":"a picture sharing platform",
    "mylist":[1,3,45]
}
oxford.update({"priya":"good girl","mylist":[56,8]})
# print(oxford.items())
for a,b in oxford.items():
    print(a,":",b)

for key in oxford.keys():
    print(key) 

# print(oxford['notpresent'])
print(oxford.get('notpresent'))
 

