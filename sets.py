# SETS  = partially writable collection and its unordered and unindexed
# bawal mag reassign || pwedeng mag dagdag
# pwedeng basahen as a whole
# no index 0-1,2,3

evenNumbers = {2,4,6,8,10}
evenNumbers.add(12)
extension = [20, 30, 40, "zero-endings"]
evenNumbers.update(extension)
print(evenNumbers)
print(len(evenNumbers))
evenNumbers.remove("zero-endings")
evenNumbers.discard(20)
print(evenNumbers)
evenNumbers.pop()
evenNumbers.pop()
evenNumbers.pop()
evenNumbers.pop()
evenNumbers.pop()
evenNumbers.pop()
evenNumbers.clear()
print(evenNumbers)

# UNION SET = pagsama-samahin || no duplicates
even =  {2,4,6, 8, 10}
odd = {1,3,5,7,9}
numbers = even.union(odd)
print("UNION", numbers)

# DIFFERENCE
setOne = {1,2,3,4,5}
setTwo = {10,30,50}
setThree = setOne.difference(setTwo)
#setThree = setTwo.difference(setOne)
print(setThree)

# INTERSECTION = kung ano yung mag kamukha || mag kaparehas
intersection =  setOne.intersection(setTwo)
print(intersection)

# DISJOINT = hahanapin kung may kapareho || returns boolean only
print(setOne.isdisjoint(setTwo))

# SUBSET AND SUPERSET = returns boolean if a set exist on other set or vice versa

# CASTING SETS TO TUPLES TO LIST AND VICE VERSA;
letters = {"a", "b", "c", "d"} # this is the set

castToTuples = tuple(letters)
print("TUPLES", castToTuples)

castToList = list(letters)
print("LIST", castToList)

# NESTED SETS = possible