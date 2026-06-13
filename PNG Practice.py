# Creating a variable.
shoppinglist = ['eggs','maize flour','wheat flour', 'rice','cooking oil','sugar','salt', 
                'yeast','milk']

# Adding to the list with no particular order
shoppinglist.append('tea leaves')
print(shoppinglist)

# Adding to the list with order
shoppinglist.insert(5,'Toothpaste')
print(shoppinglist)

# Removing an item from the list
shoppinglist.remove('salt')
print(shoppinglist)

print (shoppinglist[3:8])
print (shoppinglist[4:])
print (shoppinglist[:6])

Arsenal = ['Saka','Martinelli','Jesus','Gyokeres','Havertz', 'Madueke','Dowman', 'Trossard','Odegaard', 'Eze']
Arsenal.append('Musiala')
Arsenal.remove('Jesus')
Arsenal.remove('Martinelli')
Arsenal.remove('Trossard')
Arsenal.insert(3,'Rodrygo')
Arsenal.insert(4,'Barcola')
Arsenal.remove('Odegaard')
Arsenal.insert(7,'Nwaneri')
print(Arsenal)

Location = {
    "County": "John",
    "Constituency" : "Doe",
    "Latitude": '10deg.North', 
    "Longitude" : '12deg.East',
    }
print (Location)

num = 1
while num <= 15:
    print(num)
    num += 2
