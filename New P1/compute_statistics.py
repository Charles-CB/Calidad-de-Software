"""
Este script realiza cálculos estadísticos a partir de un archivo que contiene una lista de números.
"""
import sys
import time
from collections import Counter

def read_file(file_path):
    """Reads a file and returns a list of numbers."""
    try:
        with open(file_path, 'r') as file:
            data = [
                float(line.strip())
                for line in file.readlines()
                if line.strip().replace('.', '', 1).lstrip('-').isdigit()
            ]
        return data
    except FileNotFoundError as exception:
        print(f"Error reading file {file_path}: {exception}")
        return []
    except ValueError as exception:
        print(f"Error reading file {file_path}: {exception}")
        return []

def mean(numbers):
    """Calculates the mean of a list of numbers."""
    if not numbers:
        return None
    return sum(numbers) / len(numbers)

def median(numbers):
    """Calculates the median of a list of numbers."""
    sorted_numbers = sorted(numbers)
    talla = len(sorted_numbers)
    if talla % 2 == 0:
        mid1 = sorted_numbers[talla // 2 - 1]
        mid2 = sorted_numbers[talla // 2]
        return (mid1 + mid2) / 2
    return sorted_numbers[talla // 2]

def mode(numbers):
    """Calculates the mode of a list of numbers."""
    if not numbers:
        return None
    count = Counter(numbers)
    max_freq = max(count.values())
    modes = [num for num, freq in count.items() if freq == max_freq]
    return modes[0] if max_freq > 1 else None

def variance(numbers, mean_value):
    """Calculates the variance of a list of numbers."""
    if not numbers:
        return None
    return sum((x - mean_value) ** 2 for x in numbers) / len(numbers)

def std_deviation(variance_value):
    """Calculates the standard deviation from the variance."""
    if variance_value is None:
        return None
    return variance_value ** 0.5

def calculate_statistics(file_path):
    """Calculates various statistics for a file."""
    data = read_file(file_path)

    mean_value = mean(data)
    median_value = median(data)
    mode_value = mode(data)
    variance_value = variance(data, mean_value)
    std_deviation_value = std_deviation(variance_value)

    return {
        "file_path": file_path,
        "count": len(data),
        "mean": mean_value,
        "median": median_value,
        "mode": mode_value,
        "variance": variance_value,
        "std_deviation": std_deviation_value
    }

def main():
    """
    Realiza el procesamiento principal del programa
    """
    if len(sys.argv) != 2:
        print("Uso: python programa.py <archivo>")
        sys.exit(1)

    file_path = sys.argv[1]
    start_time = time.time()

    file_statistics = calculate_statistics(file_path)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print("Total elapsed time:", elapsed_time, "seconds\n")
    print(f"Statistics for {file_statistics['file_path']}:")
    print(f"Count: {file_statistics['count']}")
    print(f"Mean: {file_statistics['mean']}")
    print(f"Median: {file_statistics['median']}")
    print(f"Mode: {file_statistics['mode']}")
    print(f"Standard Deviation: {file_statistics['std_deviation']}")
    print(f"Variance: {file_statistics['variance']}")

    with open("CombinedStatisticsResults.txt", 'a') as combined_results_file:
        combined_results_file.write(f"Statistics for {file_statistics['file_path']}:\n")
        combined_results_file.write(f"Count: {file_statistics['count']}\n")
        combined_results_file.write(f"Mean: {file_statistics['mean']}\n")
        combined_results_file.write(f"Median: {file_statistics['median']}\n")
        combined_results_file.write(f"Mode: {file_statistics['mode']}\n")
        combined_results_file.write(f"Standard Deviation: {file_statistics['std_deviation']}\n")
        combined_results_file.write(f"Variance: {file_statistics['variance']}\n\n")

if __name__ == "__main__":
    main()
