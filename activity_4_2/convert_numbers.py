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

    # Convert to binary
    def to_binary(self, number):
        """Convert a number to binary."""
        # iterate over the number and divide by 2
        binary = ""
        negative = False
        # If the number is 0, return 0
        if number == 0:
            return "0"
        # If number is negative, compute the binary of the positive number and add a minus sign
        if number < 0:
            negative = True
            number = abs(number)
        # Compute the binary represenation with 2 as the base
        while number > 0:
            remainder = number % 2
            binary = str(remainder) + binary
            number = number // 2
        # If the number was negative, add a minus sign
        if negative:
            binary = "-" + binary
        return binary

    # Convert to hexadecimal
    def to_hexadecimal(self, number):
        """Convert a number to hexadecimal."""
        # Create a dictionary to store the hexadecimal values
        hex_values = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        # Create a string to store the hexadecimal number
        hexadecimal = ""
        negative = False
        # If the number is 0, return 0
        if number == 0:
            return "0"
        # If the number is negative, return the positive number with a minus sign
        if number < 0:
            negative = True
            number = abs(number)
        # Iterate over the number and divide by 16
        while number > 0:
            remainder = number % 16
            if remainder > 9:
                remainder = hex_values[remainder]
            hexadecimal = str(remainder) + hexadecimal
            number = number // 16
        # If the number was negative, add a minus sign
        if negative:
            hexadecimal = "-" + hexadecimal
        return hexadecimal

    def get_conversions(self):
        """Convert the numbers to binary and hexadecimal."""
        # Create a dictionary to store the conversions
        conversions = {}
        # Loop through the numbers
        for number in self.numbers:
            # Convert the number to binary and hexadecimal
            binary = self.to_binary(number)
            hexadecimal = self.to_hexadecimal(number)
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
            # Iterate over the conversions and print them
            with open("ConvertionResults.txt", "w", encoding='utf-8') as f:
                print("NUMBER\tBINARY\tHEXADECIMAL")
                f.write("NUMBER\tBINARY\tHEXADECIMAL\n")
                for number, (binary, hexadecimal) in conversions.items():
                    print(f"{number}\t{binary}\t{hexadecimal}")
                    f.write(f"{number}\t{binary}\t{hexadecimal}\n")
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
