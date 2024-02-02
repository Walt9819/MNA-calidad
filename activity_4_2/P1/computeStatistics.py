"""
Compute basic statistics from a list of numbers.
"""
import time
import sys


class Statistics():
    """
    Compute basic statistics from a list of numbers.
    Available methods:

    """
    def __init__(self, numbers) -> None:
        self.numbers = numbers
        self.sum = None
        self.count = None

        # Compute sum and count
        self._compute_sum_count()

    # Internal method to get the sum and count of numbers
    def _compute_sum_count(self):
        """Compute sum and count of numbers."""
        # Compute the sum of the numbers
        sum_numbers = 0
        # Compute the count of the numbers
        count_numbers = 0
        # Loop through the numbers
        for number in self.numbers:
            sum_numbers += number
            count_numbers += 1
        # Set in the class
        self.sum = sum_numbers
        self.count = count_numbers

    # Get the mean
    def compute_mean(self):
        """Compute mean based on the sum and count of numbers."""
        return self.sum / self.count

    # Get the median
    def compute_median(self):
        """Compute median based on the sorted list of numbers."""
        # Sort the list of numbers using the bubble sort algorithm
        sorted_n = self.numbers
        # Loop through the numbers
        for _ in range(len(sorted_n)):
            # Loop through the numbers
            for j in range(len(sorted_n) - 1):
                # If the current number is greater than the next number
                if sorted_n[j] > sorted_n[j + 1]:
                    # Swap the numbers
                    sorted_n[j], sorted_n[j + 1] = sorted_n[j + 1], sorted_n[j]
        # If the length is odd, return the middle number
        if self.count % 2 == 1:
            return sorted_n[self.count // 2]
        # If the length is even, return the average of the two middle numbers
        return (sorted_n[self.count // 2 - 1] + sorted_n[self.count // 2]) / 2

    # Get the mode
    def compute_mode(self):
        """Compute mode based on the frequency of numbers."""
        # Create a dictionary to store the frequency of numbers
        frequency = {}
        # Loop through the numbers
        for number in self.numbers:
            # If the number is not in the dictionary, add it
            if number not in frequency:
                frequency[number] = 1
            # If the number is in the dictionary, increment the frequency
            else:
                frequency[number] += 1
        # Get the maximum frequency
        max_frequency = max(frequency.values())
        # Create a list to store the mode(s)
        mode = []
        mode_count = 0
        # Loop through the items in the dictionary
        for (key, value) in frequency.items():
            # If the frequency is equal to the maximum frequency, add the number to the list
            if value == max_frequency:
                mode.append(key)
                mode_count += 1
        # If the number of modes re more than 10% of the total numbers, return a message
        if mode_count > 0.1 * self.count:
            print(f"Warning: There are {mode_count} modes for the {self.count} ({mode_count/self.count * 100:.2f}%) numbers in the data")
            return "NA"
        # Return the mode(s)
        return mode

    # Get the variance
    def compute_variance(self):
        """Compute variance based on the sum and count of numbers."""
        # Compute the mean
        mean = self.compute_mean()
        # Compute the sum of the squared differences
        sum_squared_differences = 0
        # Loop through the numbers
        for number in self.numbers:
            # Compute the squared difference
            squared_difference = (number - mean) ** 2
            # Add the squared difference to the sum
            sum_squared_differences += squared_difference
        # Compute the variance
        variance = sum_squared_differences / (self.count - 1)
        # Return the variance
        return variance

    # Get the standard deviation
    def compute_standard_deviation(self):
        """Compute standard deviation based on the variance"""
        # Compute the variance
        variance = self.compute_variance()
        # Compute the standard deviation
        standard_deviation = variance ** 0.5
        # Return the standard deviation
        return standard_deviation

    # Get all the statistics
    def get_statistics(self):
        """Get all the statistics."""
        # Perform all basic computations
        self._compute_sum_count()
        # Compute mean
        mean = self.compute_mean()
        # Compute median
        median = self.compute_median()
        # Compute mode
        mode = self.compute_mode()
        # Compute variance
        variance = self.compute_variance()
        # Compute standard deviation
        standard_deviation = self.compute_standard_deviation()
        # Return the statistics
        return {
            "mean": mean,
            "median": median,
            "mode": mode,
            "standard deviation": standard_deviation,
            "variance": variance,
        }

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
                    number = float(number)
                    # Append the number to the list
                    numbers.append(number)
                # If the word cannot be converted to a float, print an error message
                except ValueError:
                    print(f"Warning: {number} is not a number in line {i}")
            # Create a Statistics object
            stats = Statistics(numbers)
            # Get the statistics
            statistics = stats.get_statistics()
            # Print the statistics
            print(statistics)

# Run a main function when the script is run (with the file name as an argument)
if __name__ == "__main__":
    # Get the time the script was started
    start = time.time()
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
    # Get the time the script ended
    end = time.time()
