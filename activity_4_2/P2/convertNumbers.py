"""
Compute basic statistics from a list of numbers.
"""
import time
import sys

# Get the time the script was started
START = time.time()


class Converter():
    """
    Convert numbers from base 10 to binary and hexadecimal.
    """
    def __init__(self, numbers) -> None:
        self.numbers = numbers

    def get_conversions(self):
        """Convert the numbers to binary and hexadecimal."""
        # Create a dictionary to store the conversions
        conversions = {}
        # Loop through the numbers
        for number in self.numbers:
            # Convert the number to binary and hexadecimal
            binary = bin(number)
            hexadecimal = hex(number)
            # Add the conversions to the dictionary
            conversions[number] = (binary, hexadecimal)
        # Return the dictionary with the conversions
        return conversions
        

# Main function to read the data and compute the statistics
def main(file):
    """Read the data and compute the statistics."""
    # Open the file in read mode
    with open(file, "r", encoding='utf-8') as f:
        with open(file, "r", encoding='utf-8') as f:
            # Read the lines of the file separated by new line character \n
            lines = f.read().splitlines()
            # Create a list to store the numbers
            numbers = []
            # Loop through the lines (separated by new line character \n)
            for i, number in enumerate(lines):
                # Try to convert the word to a int
                try:
                    # Convert the word to a int
                    number = int(number)
                    # Append the number to the list
                    numbers.append(number)
                # If the word cannot be converted to a float, print an error message
                except ValueError:
                    print(f"Warning: {number} is not a number in line {i}")
            # Create a Statistics object
            stats = Converter(numbers)
            # Get the statistics
            conversions = stats.get_conversions()
            ### TODO ###
            # Print each number with the binary and hexadecimal representation
                # Print the time the script took to run
                print(f"TIME: {time.time() - START:.4f} seconds")
                f.write(f"TIME: {time.time() - START:.4f} seconds\n")

# Run a main function when the script is run (with the file name as an argument)
if __name__ == "__main__":
    # Get the argument next to the script name
    # If there are no arguments, the length of sys.argv is 1
    if len(sys.argv) > 1:
        # The first argument is the script name, so the second argument is at index 1
        # Get the second argument
        arg = sys.argv[1]
    else:
        # If there are no arguments, print a message
        print("No arguments were given")
    # Call the main function with the file name
    main(arg)
