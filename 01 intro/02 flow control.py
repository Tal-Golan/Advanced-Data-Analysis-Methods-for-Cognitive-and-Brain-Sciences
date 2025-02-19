# If, if else

# %%
a = 7
b = 5

# %%
if b > a:
    print("b is greater than a") # what's happening here?

# %%
if b > a:
    print("b is greater than a")
elif a > b:
    print("a is greater than b")
else:
    print("a and b are equal")

# %%
# shorthand "if"
print("b is greater than a") if b > a else print("a is greater than b") if a > b else print ("a and b are equal")

# %%
# using "or"
c=10
if a > b or a > c:
    print("at least one statement is true")

# %%
# using "and"
if a > b and c > b:
    print("both statements are true")

# %%
# nested "if"
if a > 1:
    print ("a is bigger than 1,")
    if a > 5:
        print("and also above 5")
    else:
        print("but not above 5")

# %%
# now let's try it again for a > 5
a = 3
if a > 1:
    print ("a is bigger than 1,")
    if a > 5:
        print("and also above 5")
    else:
        print("but not above 5")


# %%
# and now for a < 1 (what will happen now?)
a = 0
if a > 1:
    print ("a is bigger than 1,")
    if a > 5:
        print("and also above 5")
    else:
        print("but not above 5")


# %%
# "for" loop

# we will use "for" loop when we need to go through a collection which is iterable so the loop 
# will iterate over its elements until it reaches the end of the collection.

students = ["Avi","Dana","Mor","Na'ama"]
for student in students:
    print (student)

# %%
students = ["Avi","Dana","Mor","Na'ama"]
for i_student, student in enumerate(students):
    print(i_student, student)

# what does "enumerate" do?

# enumerate is a built-in function in python that allows to keep track of the number of iterations 
# (loops) in a loop

# %%
# "Continue":
# with the continue statement we can stop the current iteration of the loop, and continue with the next

# what will be printed here?

students = ["Avi","Dana","Mor","Na'ama"]
for student in students:
    if student == "Dana":
        continue 
    print (student)

# %%
# "Break":
# with the break statement we can stop the loop before it has looped through all the items

# what will be printed here?
students = ["Avi","Dana","Mor","Na'ama"]
for student in students:
    print (student)
    if student == "Mor":
        break 
# %%
students = ["Avi","Dana","Mor","Na'ama"]
for student in students:
    if student == "Mor":
        break
    print(student) # exit the loop when i is "Mor", but this time the break comes before the print:

# %%
# nested loops
adjs = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adj in adjs:
  for fruit in fruits:
    print(adj, fruit)

# %%
for num in range(6):
    print(num)

# %%
for num in range(2,6):
    print(num)

# %%
for num in range(6):
  print(num)
else:               # the "else" keyword in a for loop specifies a block of code to be executed when the loop is finished
  print("finished!")

# %%
# list comprehension

numbers = [1, 2, 3, 4, 5] #
squares = [num ** 2 for num in numbers]
print(squares)

# In this example, we create a list numbers containing 5 integers. 
# We then use a list comprehension to create a new list squares which contains the square of each number in the numbers list. 
# We iterate over each element in the numbers list using the for loop, and raise it to the power of 2 using the ** operator. 
# The resulting list of squared numbers is assigned to the variable squares, and printed to the console.
   
# %%
# "while" loops
# while loop execute a set of statements as long as a condition is true
# (origin :https://www.w3schools.com/python/python_while_loops.asp)

# we will use "while" loop when we want to run a code block an unknown number of times 

i = 1
while i < 6:
  print(i)
  i += 1        # why do we need to increment i?

# %%
i = 1
while i < 6:
  print(i)
  if i == 3:
    break       # using "break" we can stop the loop even if the while condition is true
  i += 1

# %%
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue        # using "continue" we can stop the current iteration, and continue with the next
  print(i)

# %%
i = 1
while i < 6:
  print(i)
  i += 1
else:       # using "else" we can run a block of code once when the condition no longer is true
  print("i is no longer less than 6")
# %%
