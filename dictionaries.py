# DICTIONARY = A collection of key-value pair || like javascript objects
# format is like json || double quotes are required

studentOne = {
    "name" : "jordan100",
    "age": 21,
    "course": "IT",
    "occupation": "programmer"
}
studentTwo = {
    "name" : "martin100",
    "age": 40,
    "course": "CS",
    "occupation": "designer"
}

students = [studentOne, studentTwo] # bind in the "list"

# accessing the value
print(studentOne["name"])
print(studentOne.get("name"))

# reassigned
rename = studentTwo["name"] ="billy100"
studentOne['gender'] = "male"
print(studentOne)

# get the keys  and values seperately in the dict
print(studentOne.keys())
print(studentTwo.values())


# NESTED DICTIONARIES
interests = {
    "sports":  ["basketball", "table-tennis"],
    "music":  {
        "favBands": ["coldplay", "mayer"]
    },
    "tech": "coding"
}
personOne = {
    "name": "tanaliga",
    "status": "single",
    "likes": interests
}
print("NESTED", personOne)
print(personOne["likes"].get("music"))

# ALL METHODS ARE APPLIED LIKE THE LIST || copy() - pop() | popItem() - clear()
