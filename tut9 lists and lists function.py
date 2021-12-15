'''
LISTS---->ordered collection of items which can be indexed and sliced
LISTS---->MUTABLE

@items in the list can be indexed
mylist=[1,2,3,4,5]
print(mylist[3])
OUTPUT----> 4

@ variable.append(item you want to add in the end)
mylist1=[1,2,3,4,5]
mylist1.append(7)
print(mylist1)

@ variable.insert(x,y)  x=index position y= what you want to insert, if string put it in ' '
mylist1=[1,2,3,4,5]
mylist1.insert(2,'harun')
print(mylist1)
OUTPUT=  [1, 2, 'harun', 3, 4, 5]


@ variable.remove(x)    x=item from the list you want to remove
mylist1=[1,2,3,4,5]
mylist1.remove(3)
print(mylist1)
OUTPUT=[1, 2, 4, 5]

@ variable.pop(x)       x=index position of the item you want to remove
mylist1=[1,2,3,4,5]
mylist1.pop(3)
print(mylist1)
OUTPUT=[1, 2, 3, 5]

@ sum(variable)         do the sum of the items in the list (if numerical)
mylist1=[1,2,3,4,5]
print(sum(mylist1))
OUTPUT=15
'''
mylist1=[1,2,3,4,5]
print(sum(mylist1))


