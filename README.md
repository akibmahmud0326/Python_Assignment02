# Python Operators – Class Assignment

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Level](https://img.shields.io/badge/Level-Beginner-brightgreen)
![Topic](https://img.shields.io/badge/Topic-Operators-yellow)
![License](https://img.shields.io/badge/License-MIT-lightgrey)


## Overview

This repository contains complete solutions for a **Python Operators** class assignment.
You’ll see clear, runnable examples of **arithmetic, logical, assignment, and comparison operators** plus a bonus **student-grading system** that ties them all together.

Assignment Structure <br/>

1. Arithmetic Operators <br/>
Calculate area and perimeter of a rectangle <br/>
Convert temperature from Celsius to Fahrenheit <br/>
Find remainder of a division <br/>
Compute expressions using exponentiation and division <br/>
Calculate average of 5 numbers <br/>
2. Logical Operators <br/>
Check if a number is positive and even <br/>
Check voting eligibility <br/>
Verify conditions using logical and, or, and not <br/>
Validate student pass/fail status <br/>
Reverse boolean conditions <br/>
3. Assignment Operators <br/>
Perform chained operations on a variable using +=, -=, *=, /=, %= <br/>
Create a counter using += <br/>
Simulate interest accumulation with *= <br/>
Build a countdown using -= <br/>
4. Comparison Operators <br/>
Check equality and inequality <br/>
Compare ages and values <br/>
Determine conditions based on year and marks <br/>
Validate division safety <br/>
Bonus: Mixed Assignment – Grading System <br/>
A full program that: <br/>

Accepts student details and marks <br/>
Calculates total, average, and percentage <br/>
Assigns grades (A, B, C, F) <br/>
Checks for pass/fail and scholarship eligibility <br/>
Applies bonus marks using assignment operators <br/>
Recalculates results after bonus <br/>
Prints a detailed report <br/>


## Features 

* Self-contained, ready-to-run script (`assignment.py`)
* Demonstrates every core operator category in Python
* Bonus grading system with total, average, grade, pass/fail & scholarship checks
* No external libraries required—only the Python standard library


## Technologies Used

* Python 3.10 or newer


## Installation

```bash
# 1 · Clone this repo
git clone https://github.com/your-username/python-operators-assignment.git
cd python-operators-assignment

# 2 · (Optionally) create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3 · No extra packages needed—run it!
```


## Usage

```bash
python assignment.py
```

Typical console output (abridged):

```
Area: 15
Perimeter: 16
Fahrenheit: 77.0
Remainder: 1
Result: 40.0
Average: 30.0
Positive and even? True
Eligible to vote? True
...
--- Student Report ---
Name: Alice
Total Marks (before bonus): 240
Average (before bonus): 80.0
Percentage: 80.0
Grade: A
Passed All Subjects? True
Eligible for Scholarship? False
Total After Bonus: 255
Average After Bonus: 85.0
```


## File Structure

```
python-operators-assignment/
├── assignment.py   # All operator demos + grading system
└── README.md       # This documentation
```


## Sample Code Snippet

```python
# Arithmetic: rectangle area & perimeter
length = 5
width  = 3
area        = length * width
perimeter   = 2 * (length + width)
print("Area:", area)
print("Perimeter:", perimeter)
```

*(See `assignment.py` for the full script.)*


## License

Released under the **MIT License** — see `LICENSE` for details.


## Author

**Akib Mahmud**
B.Sc. in CSE,<br/> Daffodil International University

* GitHub: https://github.com/akibmahmud0326
* Email: akibmahmudabcd@gmail.com


## Contributions

Pull requests are welcome! Feel free to open issues or fork the repo to improve examples, add comments, or suggest new operator exercises.


## Support

If this helped you, please ⭐ the repository and share it with classmates. Happy coding!
