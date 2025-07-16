🌟 Prime Divisors Challenge

A Python program that reads 10 integers and finds the one with the most distinct prime divisors. If there's a tie, it selects the largest number.
Description
This program solves the following problem:

Read 10 integers from input.
For each number, calculate the number of distinct prime divisors.
Output the number with the highest count of distinct prime divisors, along with that count.
If multiple numbers have the same count, output the largest one.

Example
Input:
123
43
54
12
76
84
98
678
543
231

Output:
678 3

Explanation:
678 has three distinct prime divisors: 2, 3, and 113.
Usage

Ensure you have Python 3.8 or higher installed.

Save the code in a file named prime_divisors.py.

Run the program using:
python prime_divisors.py


When prompted, enter 10 integers, one per line.

The program will output the number with the most distinct prime divisors and its count.


Code
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_divisors(n):
    count = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            if is_prime(i):
                count += 1
            while n % i == 0:
                n //= i
        i += 1
    if n > 1 and is_prime(n):
        count += 1
    return count

# Read 10 numbers from input
numbers = []
for _ in range(10):
    numbers.append(int(input()))

# Find number with maximum prime divisors
max_prime_count = -1
max_number = -1
for num in numbers:
    prime_count = count_prime_divisors(num)
    if prime_count > max_prime_count or (prime_count == max_prime_count and num > max_number):
        max_prime_count = prime_count
        max_number = num

# Print result
print(f"{max_number} {max_prime_count}")

Test Cases



Input Number
Prime Divisors
Count



110
2, 5, 11
3


24
2, 3
2

