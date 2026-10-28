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

# Main routine starts here

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate the area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display output
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"Area: {area} square units")

    # Ask the user whether they want to keep going
    keep_going = input("Press enter if you want to keep going or any key to quit. ")
    print()

print("Thank you for using the area/perimeter calculator")