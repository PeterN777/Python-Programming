# dictionaries in python.
# uses key-value pairs.
person = {
    "first name": "John",
    "last name" : "Doe",
    "age": 25,
    "favouritecolors" : ['blue', 'green'],
    "salary": 20000
    }
print (person)

# accessing a dictionary item using the key.
print (person['age'])
print (person["salary"])

# updating the value of a key-value pair.
person ["age"]=34
print (person)

# adding a key value pair to our dictionary

person ["passport"] = "B0078hm"
print (person)

# removing a key value pair from our dictionary.

del person ["last name"]
print(person)
