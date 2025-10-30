#From a list of numbers, move zero to the end of the list.

list = [2,0,3,7,9,8,5]
for item in list:
    if item ==0:
       list.remove(item)
       list.append(item)
print(list)
