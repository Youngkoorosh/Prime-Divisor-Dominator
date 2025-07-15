# Prime-Divisor-Dominator
This repository contains a solution to a programming exercise that identifies the number with the most prime divisors from a given set of inputs.

Project Description
The program reads 10 integers from the user. It then determines which of these numbers has the highest count of prime divisors. If multiple numbers share the same maximum count of prime divisors, the program identifies and outputs the largest among them. The final output includes the chosen number and its corresponding count of prime divisors.

Sample Input
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
Sample Output
678 3
How to Run
Clone the repository:

Bash

git clone https://github.com/[Your-Username]/prime-divisor-dominator.git
Navigate to the project directory:

Bash

cd prime-divisor-dominator
Compile and run the code (instructions may vary depending on the programming language used, e.g., for Python):

Bash

python your_program_file.py
(Replace your_program_file.py with the actual name of your Python script.)

The program will then prompt you to enter 10 numbers.

Note on Dictionaries (for Python users)
If you are using dictionaries in your solution, be aware that standard Python dictionaries (before Python 3.7) do not inherently preserve insertion order. If order is crucial for any part of your logic beyond this specific problem, consider using collections.OrderedDict or a similar data structure. However, for this particular problem, the order of input numbers doesn't affect the final result.
