# String
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

# String Concat
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Input
name = input("What is your name? ")
print(name)

# format output strings
color = input("What is your favorite color? ")
animal = input("What is your favorite animal? ")
print("{}, you like a {} {}!".format(name, color, animal))