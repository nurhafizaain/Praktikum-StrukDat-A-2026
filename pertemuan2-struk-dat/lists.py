#lists :cara 1
thislist = ["apple", "banana", "cherry"]
print(thislist)
#cara 2
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
#cara 3
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
#cara 4
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
#cara 5
list1 = ["abc", 34, True, 40, "male"]
#cara 6
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
#cara 7
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#access_item :cara 1
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
#cara 2
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
#cara 3
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
#cara 4
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
#cara 5
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
#cara 6
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
#cara 7
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#change_item :cara 1
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
#cara 2
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
#cara 3
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
#cara 4
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
#cara 5
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#add_list_item :cara 1
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
#cara 2
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
#cara 3
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#cara 4
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

#remove_list_item :cara 1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
#cara 2
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)
#cara 3
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
#cara 4
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
#cara 5
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
#cara 6
thislist = ["apple", "banana", "cherry"]
del thislist
#cara 7
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#loop_lists :cara 1
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#cara 2
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
#cara 3
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#cara 4
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#list_comprehension :cara 1
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
#cara 2
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)
#cara 3
newlist = [x for x in fruits if x != "apple"]
#cara 4
newlist = [x for x in fruits]
#cara 5
newlist = [x for x in range(10)]
#cara 6
newlist = [x for x in range(10) if x < 5]
#cara 7
newlist = [x.upper() for x in fruits]
#cara 8
newlist = ['hello' for x in fruits]
#cara 9
newlist = [x if x != "banana" else "orange" for x in fruits]

#sort_lists :cara 1
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
#cara 2
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
#cara 3
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
#cara 4
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#cara 5
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
#cara 6
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
#cara 7
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
#cara 8
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#copy_lists :cara 1
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
#cara 2
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
#cara 3
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

#join_lists :cara 1
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)
#cara 2
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
#cara 3
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

#list_methods
#list_exercises