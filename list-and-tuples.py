# LISTS
# READ and WRITE collection ||  array-ish alike

favBands = [
    "coldplay",
    "u2",
    "the corrs",
    "mayer",
    'billy',
    "coldplay",
    "coldplay"

]
# ASSIGNING VALUE TO A PARTICULAR INDEX ON THE LIST
favBands[0] = 'COLDPLAY'
print((favBands))

# COUNT HOW MANY TIMES IT OCCURS || case sensitive
print(favBands.count("coldplay"))

# ADD ITEM TO THE LIST

# APPEND = add ng item sa dulo
favBands.append("the script")
print(favBands)

# POP = mag delete ng item
favBands.pop(0)
print(favBands)

# INSERT = sa particular na index
favBands.insert(0, 'elton')
print(favBands)

# REMOVE = case sensitive
favBands.remove("coldplay")
favBands.remove("coldplay")

# DEL = removes a specified index but if not declared it delete all the lists
del favBands[0]
# del favBands
# favBands.clear()
print(favBands)


# COPY = copies the whole list and assigned it to the new list
x = favBands.copy()
print("COPY" , x)

# COMBINING LIST = can use + operator
a = ['guitar',  'piano']
b = ['yellow', 'the scientist']
combi = a + b
print(combi)

# COMBINING LIST BY extend() || it append the structure can be arrays or objects
a.append(b)
print(a)

# REVERSE LIST ITEMS
a.reverse()
print(a)

# SORT
alph = ["Z", "A", "D", "X", "W"]
alph.sort(reverse=True)
print(alph)

# NESTED LIST =  a list inside a list known as sublist
music = ["yellow", "the scientist",  ["coldplay", "the cors", ["martin"]]]
print("ALL ABOUT MUSIC",  music[2][2])

# TUPLES = read-only collection | used to sort certain data || doesnt support item assignment
j = ('one', 'two', 'three')
k = ["four", "five", "six"]
# converting tuples to list
j = list(j)
print(j)
# converting list to tuples
k = tuple(k)
print(k)

