# string functions

mystr="abcdefghijklmnopqrstuvwxyz"

print(len(mystr))

print(mystr.endswith("eer"))
print(mystr.endswith("xyz"))
print(mystr.endswith("uvxyz"))

print(mystr.startswith("abcde"))

print(mystr.count('a'))
print(mystr.count('ab'))

print(mystr.capitalize())

print(mystr.find("cde"))

print(mystr.replace("abc","ABC"))
