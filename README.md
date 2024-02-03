# RSA Factoring Challenge README

## Table of Contents
1. [Factorize All The Things!](#factorize-all-the-things)
2. [RSA Factoring Challenge](#rsa-factoring-challenge)
3. [Repository Structure](#repository-structure)
4. [Usage Instructions](#usage-instructions)
5. [Testing](#testing)

## Factorize All The Things!
- **Task**: Factorize as many numbers as possible into a product of two smaller numbers.
- **Usage**: `factors <file>`
    - `<file>`: A file containing natural numbers, one number per line.
- **Output Format**: `n=p*q`
    - `n`: Original number.
    - `p` and `q`: Factors of `n` (not necessarily prime).
- **Constraints**:
    - Time Limit: 5 seconds.
    - No external dependencies.
    - Natural numbers greater than 1.
    - No empty lines in the file.
- **Example**:
    ```
    4=2*2
    12=6*2
    34=17*2
    ...
    ```

## RSA Factoring Challenge
- **Task**: Factorize a number into two prime numbers `p` and `q` such that `n = p × q`.
- **Usage**: `rsa <file>`
    - `<file>`: A file containing a single natural number.
- **Output Format**: `n=p*q`
    - `n`: Original number.
    - `p` and `q`: Prime factors of `n`.
- **Constraints**:
    - Time Limit: 5 seconds.
    - No external dependencies.
    - Only one number in the file.
- **Example**:
    ```
    6=3*2
    77=11*7
    ...
    ```

## Repository Structure
RSA-Factoring-Challenge/
│
├── factors       # Executable for the first task.
└── rsa           # Executable for the RSA factoring challenge.

## Usage Instructions
- To run the factorization task, use:
    ```
    ./factors <path_to_file>
    ```
- To run the RSA factoring challenge, use:
    ```
    ./rsa <path_to_file>
    ```

## Testing
- To test the executables, provide a file with the appropriate format as shown in the examples under each task description.
