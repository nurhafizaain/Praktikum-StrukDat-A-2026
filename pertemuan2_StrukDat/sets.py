#sets :cara 1
thisset = {"apple", "banana", "cherry"}
print(thisset)
#cara 2
thisset = {"apple", "banana", "cherry", "apple"}

print(thisset)
#cara 3
thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)
#cara 4
thisset = {"apple", "banana", "cherry", False, True, 0}

print(thisset)
#cara 5
thisset = {"apple", "banana", "cherry"}

print(len(thisset))
#cara 6
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
#cara 7
set1 = {"abc", 34, True, 40, "male"}
#cara 8
myset = {"apple", "banana", "cherry"}
print(type(myset))
#cara 9
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
#cara 10

#access_set_items :cara 1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)
#cara 2
thisset = {"apple", "banana", "cherry"}

print("banana" in thisset)
#cara 3
thisset = {"apple", "banana", "cherry"}

print("banana" not in thisset)

#add_set_items :cara 1
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
#cara 2
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)
#cara 3
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]

thisset.update(mylist)

print(thisset)

#remove_set_items :cara 1
thisset = {"apple", "banana", "cherry"}

thisset.remove("banana")

print(thisset)
#cara 2
thisset = {"apple", "banana", "cherry"}

thisset.discard("banana")

print(thisset)
#cara 3
thisset = {"apple", "banana", "cherry"}

x = thisset.pop()

print(x)

print(thisset)
#cara 4
thisset = {"apple", "banana", "cherry"}

thisset.clear()

print(thisset)

#loop_sets :cara 1
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

#join_sets :cara 1
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)
#cara 2
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

set3 = set1 | set2
print(set3)
#cara 3
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)
#cara 4
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1 | set2 | set3 |set4
print(myset)
#cara 5
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)
#cara 6
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)
#cara 7
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.intersection(set2)
print(set3)
#cara 8
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 & set2
print(set3)
#cara 9
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)
#cara 10
set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)
#cara 11
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)
#cara 12
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 - set2
print(set3)
#cara 13
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.difference_update(set2)

print(set1)
#cara 14
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.symmetric_difference(set2)

print(set3)
#cara 15
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1 ^ set2
print(set3)
#cara 16
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.symmetric_difference_update(set2)

print(set1)

#frozenset :cara 1
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x))

#set_methods
#set_exercises