# chapter 3 practice set

# write a program to display good afternoon followd by your name
name=input("enter your name: ")
print("good afternoon "+name)

# letter template
name=input("enter the name: ")
date=input("enter the date: ")

template='''
Dear <|name|>,
you are selected
<|date|>
'''
print(template.replace("<|name|>",name).replace("<|date|>",date))

# detect double spaces inside a string
mystr="this is me  and I am a  good girl"

print(mystr.find("  "))
print(mystr.find("priya"))

# replace the double space with sigle space
print(mystr.replace("  "," "))

# format using escape sequence charcters
letter="Dear Priya,\n\tThis python course is nice.\nThanks!"
print(letter)