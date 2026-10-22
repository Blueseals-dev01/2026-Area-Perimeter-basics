# ask the user for their name
username = input ("What is your name? ")

# ask the user for their favorite number (interger)
fav_num = int(input("What is your favorite number? "))

# double, half and square the users favorite number
double = fav_num * 2
halve = fav_num / 2
square = fav_num * fav_num

# greet the user
print(f"Hi {username}, your favorite number is {fav_num}")

# Output the results of doubling, halfing and 
# squaring their favorite interger
print(f"Double {fav_num} is {double}.")
print(f"Half {fav_num} is {halve}.")
print(f"{fav_num} squared is {square}.")
print()
print("Have a nice day.")