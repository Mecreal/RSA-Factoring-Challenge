#!/usr/bin/python3
"""
Module pour factoriser
"""
import sys


def file_h(file_path):
    """
    Process a file line by line to find factors of each number.

    This function opens a file, reads each line as a number, and prints
    out the factorization of that number. It handles various exceptions
    such as file not found, permission error, and invalid file content.

    Parameters:
    file_path (str): The path of the file to be processed.

    """
    try:
        with open(file_path, 'r') as file:
            for line in file:
                number = int(line.strip())
                p, q = factor(number)
                print(f"{number}={p}*{q}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(2)
    except PermissionError:
        print(f"Error: Permission denied when accessing '{file_path}'.")
        sys.exit(3)
    except ValueError:
        print(f"""Error: Invalid content in '{file_path}'.
        All lines must be valid natural numbers.""")
        sys.exit(4)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(5)


def factor(n):
    """
    Find and return a pair of factors for a given number.

    The function searches for two numbers such that their product
    equals n.
    It starts from the smallest factor (2) and goes up to the square
    root of n.
    If no factors are found, it returns 1 and n as a fallback.

    Parameters:
    n (int): The number to be factorized.

    Returns:
    tuple: A tuple containing two factors of n.

    """
    # i = 2
    # while (n % i) != 0:
    #     i += 1
    # return (n // i, i)

    if n % 2 == 0:
        return n // 2, 2
    elif n % 3 == 0:
        return n // 3, 3

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return n // i, i
        i += w
        w = 6 - w  # Alternates between adding 2 and 4

    return n, 1  # n is prime
