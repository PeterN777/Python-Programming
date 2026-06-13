# list data types in python.
items= ["Honda","Nissan","Mitsubishi", "Surf", "Mazda", "Volkswagen"]
print (items)

#  access an item using index
# when we use index we start from 0.

print (items[0])
print (items[1])
print (items[2])
print (items[3])
print (items[4])
print (items[5])

# slice to access list item 2-5.
# to access the last item we add one item for python to remove that item.
print (items[2:7])

# accessing listem 3 and above.
print (items[3:7])
# accessing list item 5 and below we minus one
print (items[:6])

# a list is mutable and can be changed.
# adding Toyota to our list.
items.append("Toyota")
print (items)

# insert bmw at index 3
items.insert(3,"bmw")
print(items)

  
        