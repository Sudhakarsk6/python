alien={'color':'green','points':5}
#access a value
print("the alien's color is "+alien["color"])
#adding a new key-value pair
alien['x_position']=0
print(alien)
#looping all key-value pairs
for x,y in alien.items():
    print(x+" "+str(y))
#looping all key
for x in alien.keys():
    print(x)
#looping all key
for y in alien.values():
    print(str(y))

#while loop 
cut_val=1
while cut_val<=5:
    print(cut_val)
    cut_val += 1

msg=''
while msg!= 'quit':
    msg=input("what's your message :")
    print(msg)