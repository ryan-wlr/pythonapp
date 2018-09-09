
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
        print("Out of guesses. You lose!")
if out_of_guesses == False:    
    print("You win!")

# For Loop
# Print out a different character for ever letter in loop
for letter in "Giraffe Academy":
    print(letter)

# Loop through all the elements inside of the array
friends = ["Jim", "Karen", "Kevin"]

# Copy friends list using copy() fuction
print("\n/** Copy friends list using copy() fuction **/\n")
friends2 = friends.copy()
print(friends2)

# Create lucky numbers list
print("\n/** Create lucky_numbers list **/\n")
lucky_numbers = [42, 8, 15, 16, 23]
print(lucky_numbers)

# Sort lucky numbers list
print("\n/** Sort lucky numbers using sort() fuction **/\n")
lucky_numbers.sort()
print(lucky_numbers)

# Reverse lucky numbers list
print("\n/** Reverse lucky numbers list using reverse() fuction **/\n")
lucky_numbers.reverse()
print(lucky_numbers)

#  Append friends list
print("\n/** Append friends list **/\n")
friends.append("Kelly")

# Insert element to middle of list
print("\n/** Insert element to middle of list **/\n")
friends.insert(1, "Sharen")

# Remove an element from list
print("\n/** Remove an element from list **/\n")
friends.remove("Jim")

# Find friend in list
print("\n/** Find friend in list Kevin position. Using index fuction **/\n")
print(friends.index("Kevin"))

# Count number of times Jim shows up in list
print("\n/** Count number of times Sharen shows up in list. Using count fuction")
print(friends.count("Sharen"))

# Sort the list in asending order
print("\n/** Sort the list in asending order. Using sort fuction **/\n")
friends.sort()

for friend in friends:
    print(friend)

# Print out each value in range function
print("\n/** Print out each value in range function **/\n")
for index in range(10):
    print(index)

# Print out all the numbers between 3 and 10
print("\n/** Print out all the numbers between 3 and 10 **/\n")
for index in range(3, 10):
    print(index)

val = len(friends)
print(val)

# Print length of array
print("\n/** Print length of array **/\n")
val = len(friends)
print(val)

# Another way of printing the friends array
print("\n/** Another way of printing the friends array **/\n")
for index in range(len(friends)):
    print(friends[index])

# Print stuff out on other iteration of loop
print("\n/** Print stuff out on other iteration of loop **/\n")
for index in range(5):
    if index == 0:
        print("first Iteration")
    else:
        print("Not first")

# Exponent Function
print("\n/** Exponent Fuction **/")
print("/** 2^3 **/\n")
print(2**3)

# Function with for loop raised to the power
print("\n/** Function with for loop raised to the power **/\n ")

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 4))

# Two deminsional lists
print("\n/** Two deminsional lists **/\n")

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]

# Print out index in the row, column 1 value
print("\n/** Print out index in the row 0, column 0 value **/\n[1, 2, 3],\n[4, 5, 6],\n[7, 8, 9],\n[0]\n")
print(number_grid[0][0])

# Nested forloop
print("\n/** Nested forloop **/\n")

for row in number_grid:
    for col in row:
        print(col)

# Build a Translator
print("\n/** Build a Translator **/\n")
print("Giraffe Language\nvowel -> g\n------------\n\ndog -> dgg\ncat -> cgt\n")

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

# Also do lowercase letters
print("\n/** Also do lowercase letters **/\n")
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "AEIOUaeiou":
            # Able to control both upper and lower situations 
            print("Ex. On")
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

print("\n/** Comments **/\n")

print("/** To write out triple comments **/")
print("'''\nYour comment\nanother line\nblah blah blah\n'''")

'''
 practice 
 comment
'''

# Try Except
print("\n/** Try Except **/\n")

# Convert an input number to an integer
print("\n/** Convert an input number to an integer **/\n")

number = int(input("Enter a number: "))
print(number)

# Try Except block
print("\n/** Try Except block. If you don't enter in the exact number /**\n")
'''
try:
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number) 
#except:
    print("Invalid Input")
'''
# Specify Except block with special fuction
print("\n/** Specify Except block with special fuction **/\n")
try:
    answer = 10
    #value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
# Store exception as a varable
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid input")

# Reading Files
print("\n/** Reading Files **/\n")

employee_file = open("employees.txt", "r")
print(employee_file.readable())
# print info inside file

# Read individual line 
print("\n/** Read individual line **/\n")
print(employee_file.readline())

print("\n/** Print info inside file /**")
print(employee_file.read())
employee_file.close()

# Reopen file
employee_file = open("employees.txt", "r")

# Put all lines inside an array
print("\n/** Put all lines inside an array /**")
#print(employee_file.readlines()[2] + "\n")
print(employee_file.readlines())
employee_file.close()

# Reopen file
employee_file = open("employees.txt", "r")

# Read out each individual employee in array
print("\n/** Read out each individual employee in array **/\n")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()

# Reopen file
employee_file = open("employees.txt", "r")

# Print individual line 
print("\n/** Print individual line /**")
print(employee_file.readlines()[2] + "\n")
employee_file.close()

# Appending and Writing to Files
print("\n/** Appending and Writing to Files **/\n")

# Reopen file with append 
employee_file = open("employees.txt", "a")
# Write new employee
print("/** Write new employee **/")
employee_file.write("Toby - Human Resources")
employee_file.close()

employee_file = open("employees.txt", "r")
employee_file.read()
employee_file.close()

print("\n/** End video 4:26:51 **/\n")

# Creating a tuple
print("\n/** Creating a tuple. Tuples are used in coordinates and cannot be changed **/\n")
coordinates = (4, 5)
print(coordinates[1])

# Creating a tuple list
print("\n/** Creating a tuple list coordinates[(4, 5), (6, 7), (80, 34)] **/\n")
coordinates = [(4, 5), (6, 7), (80, 34)]
print(coordinates)

# Create an html file and write some code
print("\n/** Create an html file and write some code **/\n")
html_file = open("index.html", "w")
html_file.write("<p>This is html</p>")
html_file.close()