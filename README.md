🌟 Prime Divisors Challenge

Welcome to the Prime Divisors Challenge! This Python project solves a classic programming problem with elegance and efficiency. It reads 10 integers, finds the one with the most distinct prime divisors, and outputs it along with the count. In case of ties, the largest number wins. Ready to dive into some clean code? 🚀

📜 Problem Statement
The goal is simple yet intriguing:

Input: 10 integers, one per line.
Task: Identify the number with the highest count of distinct prime divisors.
Output: Print the number and its prime divisor count in the format <number> <count>.
Tiebreaker: If multiple numbers have the same count, pick the largest one.

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

Why?678 has 3 distinct prime divisors (2, 3, 113), the highest among the inputs, making it the champion! 🏆

💻 Code Solution
The solution is crafted in Python with a focus on readability, efficiency, and GitHub's Markdown rendering. Below is the complete code, broken down into digestible parts for clarity.
Core Functions

is_prime(n): Determines if a number is prime by checking divisibility up to its square root.
count_prime_divisors(n): Counts distinct prime divisors by factoring the number and verifying primality.

Full Code
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_prime_divisors(n):
    """Count distinct prime divisors of a number."""
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

# Read 10 integers from input
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

Code Highlights

Efficiency: Uses square root optimization for prime checks and factorization. ⚡
Clarity: Descriptive function names and comments make the code self-explanatory.
No Dictionaries: Avoids dictionaries to respect the problem's note about order preservation.


🛠️ How to Run

Requirements: Python 3.8 or higher.
Setup: Save the code as prime_divisors.py.
Execution:python prime_divisors.py


Input: Provide 10 integers, one per line.
Output: The program displays the number with the most prime divisors and its count.

Example Run
$ python prime_divisors.py
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
678 3


✅ Test Cases



Input Number
Prime Divisors
Count



110
2, 5, 11
3


24
2, 3
2



🎨 GitHub Styling Notes
This README is designed to shine on GitHub with:

**Badges
