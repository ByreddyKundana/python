# list methods

mylist=[1,8,7,2,7,21,15]
print(mylist)
a=mylist.sort()  #sorts the list
print(a)
print(mylist)

mylist.reverse()   #reverse the list
print(mylist)

mylist.append(8)
print(mylist)     #appends at last

mylist.insert(2,9)  #inserts 9 at index2
print(mylist)

mylist.pop()       #removes an item from the end of the list
mylist.pop(2)     #removes an item from the index 2
print(mylist)

mylist.remove(15)
mylist.remove(7)    #removes first occurence of duplicate items
print(mylist)