"""
convert numbers from a file to binary and hexadecimal base
"""

import sys
import time

def read_file(file_path):
    """Reads a file and returns a list of numbers."""
    try:
        with open(file_path, 'r') as file:
            numbers = [float(line.strip()) for line in file]
        return numbers
    except FileNotFoundError as exception:
        print(f"Error: File {file_path} not found. {exception}")
        return []
    except ValueError as exception:
        print(f"Error reading file {file_path}: {exception}")
        return []

def convert_numbers(numbers):
    """Converts numbers to binary and hexadecimal base."""
    binary_results = [bin(int(num)) for num in numbers]
    hex_results = [hex(int(num)) for num in numbers]
    return binary_results, hex_results

def main():
    """Main function to execute the number conversion program."""
    if len(sys.argv) != 2:
        print("Usage: python convertNumbers.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()

    numbers = read_file(file_path)

    if not numbers:
        print("No valid data in the file.")
        sys.exit(1)

    binary_results, hex_results = convert_numbers(numbers)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Print results on the screen
    print("Converted numbers:")
    for i, num in enumerate(numbers):
        print(f"Num: {num}\n"
            f"Binary: {binary_results[i]}\n"
            f"Hexadecimal: {hex_results[i]}\n"
            f"----------------------------")

    # Save results to ConvertionResults.txt
    with open("ConvertionResults.txt", 'w') as results_file:
        results_file.write("Converted numbers:\n")
        for i, num in enumerate(numbers):
            results_file.write(f"Num: {num}\n"
                               f"Binary: {binary_results[i]}\n"
                               f"Hexadecimal: {hex_results[i]}\n"
                               f"-----------------------------\n")

        results_file.write(f"\nElapsed time: {round(elapsed_time,4)} seconds\n")

    # Print elapsed time
    print(f"\nElapsed time: {round(elapsed_time,4)} seconds")
    print("Results saved in ConvertionResults.txt")

if __name__ == "__main__":
    main()
