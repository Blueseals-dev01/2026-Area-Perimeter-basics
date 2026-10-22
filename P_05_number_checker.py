# Ask the user for width and loop until they
# Enter a number that is more than 0
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # Ask the user for a number
            response = float(input(question))

            # Check that number is more than zero
            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)


# Main routine goes here
for item in range(0, 2):
    width = num_check("Width: ")
    print(width)

    print()

# Main routine goes here
for item in range(0, 2):
    height = num_check("Height: ")
    print(height)