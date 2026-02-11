#tuples :cara 1
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#cara 2
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
#cara 3
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
#cara 4
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
#cara 5
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
#cara 6
tuple1 = ("abc", 34, True, 40, "male")
#cara 7
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
#cara 8
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)

#access_tuple :cara 1
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
#cara 2
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
#cara 3
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
#cara 4
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
#cara 5
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
#cara 6
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
#cara 7
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")

#update_tuples :cara 1
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
#cara 2
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#cara 3
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)
#cara 4
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#unpack_tuples :cara 1
fruits = ("apple", "banana", "cherry")
#cara 2
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
#cara 3
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)
#cara 4
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")

(green, *tropic, red) = fruits

print(green)
print(tropic)
print(red)

#loop_tuples :cara 1
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)
#cara 2
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
#cara 3
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#join_tuples :cara 1
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)
#cara 2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)

#tuple_methods
#tuple_exercises