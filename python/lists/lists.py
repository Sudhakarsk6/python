colours=['green','red','yellow']
print(colours)
#get the first item in the list
print(colours[0])
#get the last item in the list
print(colours[-1])
#looping through a list
for i in colours:
    print("values"+" "+i)
#adding item to a list
col=[]
col.append('blue')
col.append('pink')
print("added items are: ",col)
#making numerical lists
square=[]
for x in range(1,11):
    square.append(x**2)
print(square)
#or list comprehensions
squares=[x**2 for x in range(1,11)]
print(squares)
#list slice first two val
col=['red','green','blue','yellow']
print(col[:2])
#copying a list
copy_col=col[:]
print(copy_col)