"""
wordCount.py: Counts the frequency of distinct words in a given file.
"""

import sys
import time
from collections import Counter

def read_file(file_path):
    """Reads a file and returns a list of words."""
    try:
        with open(file_path, 'r') as file:
            words = [word.strip() for line in file for word in line.split()]
        return words
    except FileNotFoundError as exception:
        print(f"Error: File {file_path} not found. {exception}")
        return []
    except ValueError as exception:
        print(f"Error reading file {file_path}: {exception}")
        return []

def count_words(words):
    """Counts the frequency of each distinct word."""
    return Counter(words)

def main():
    """Main function to execute the word counting program."""
    if len(sys.argv) != 2:
        print("Usage: python wordCount.py fileWithData.txt")
        sys.exit(1)

    file_path = sys.argv[1]

    start_time = time.time()

    words = read_file(file_path)

    if not words:
        print("No valid data in the file.")
        sys.exit(1)

    word_counts = count_words(words)

    end_time = time.time()
    elapsed_time = end_time - start_time

    # Imprimir nombre del archivo en consola y archivo de resultados
    print(f"\nDATA FROM: {file_path}")
    print("---- Word frequencies ----")
    print(f"COUNT: {len(words)}")
    for word, count in word_counts.items():
        print(f"{word}: {count}")

    with open("WordCountResults.txt", 'w') as results_file:
        results_file.write(f"Word frequencies for file: {file_path}\n")
        results_file.write("Word frequencies:\n")
        results_file.write(f"COUNT: {len(words)}\n")
        for word, count in word_counts.items():
            results_file.write(f"{word}: {count}\n")

        results_file.write(f"\nElapsed time: {round(elapsed_time,4)} seconds\n")

    print(f"\nElapsed time: {round(elapsed_time,4)} seconds")
    print("Results saved in WordCountResults.txt")

if __name__ == "__main__":
    main()
