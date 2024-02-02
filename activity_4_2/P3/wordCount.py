"""
Compute basic statistics from a list of numbers.
"""
import time
import sys

# Get the time the script was started
START = time.time()

def get_frequency(words):
    """
    Compute the frequency of words in the list.
    """
    # Create a dictionary to store the frequency of words
    frequency = {}
    # Iterate over the words
    for word in words:
        # If the word is not in the dictionary, add it
        if word not in frequency:
            frequency[word] = 1
        # If the word is already in the dictionary, increment its count
        else:
            frequency[word] += 1
    # Return the dictionary with the frequency of words
    return frequency


# Main function to read the data and compute the statistics
def main(file):
    """Read the data and compute the statistics of words."""
    # Open the file in read mode
    with open(file, "r", encoding='utf-8') as f:
        with open(file, "r", encoding='utf-8') as f:
            # Read the lines of the file separated by new line character \n
            lines = f.read().splitlines()
            # Create a list to store the words
            words = []
            # Loop through the lines (separated by new line character \n)
            for i, word in enumerate(lines):
                # Check if word is not empty
                if word == "":
                    print(f"Warning: {word} is not a word in line {i}")
                    continue
                # Split the line into words
                word = word.split(" ")
                if len(word) > 1:
                    print(f"Warning: Line {i} has multiple words: {word}")
                    # Add the words to the list
                    words.extend(word)
                else:
                    # Add the word to the list
                    words.append(word[0])
            # Compute the frequency of words
            word_count = get_frequency(words)
            # Iterate over the conversions and print them
            with open("WordCountResults.txt", "w", encoding='utf-8') as f:
                print("WORD\tCOUNT")
                f.write("WORD\tCOUNT\n")
                for word, count in word_count.items():
                    print(f"{word}\t{count}")
                    f.write(f"{word}\t{count}\n")
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
