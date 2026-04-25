"""Task: Robust Log File Processor
Scenario: You are building a system that reads a list of numbers from a file named data.txt, calculates their reciprocal (
1
/
x
1/x), and writes the results to a new file named results.txt. You must ensure the program does not crash even if the input file is missing or contains invalid data (like zeros or text).

Requirements:

File Input: Open data.txt in read mode. Use exception handling to catch a FileNotFoundError and print a user-friendly message if it doesn't exist.
Processing:
Read the file line by line.
Convert each line to an integer. Handle ValueError if a line contains a string or non-numeric character.
Calculate 
1
1 divided by that number. Handle ZeroDivisionError if a line contains 
0
0.
File Output: Append the valid results to results.txt.
Cleanup: Use a finally block to ensure that all open file objects are properly closed, regardless of any errors encountered during processing.
Custom Validation: Use the raise keyword to trigger an exception if a number in the file is negative, as your system only supports positive values.
Submission Guidelines:
Submission: Paste your solution in the submission box.
Code Structure: Ensure your code is modular. Use a clear try-except-else-finally structure.
Comments: Include comments explaining which specific exception is being handled in each except block.
Verification: Create a dummy data.txt with the following content to test your code (No need to upload this):
10
0
abc
-5
20"""

input_file = "data.txt"
output_file = "results.txt"
try:
    with open(input_file,"r") as f, open(output_file, "a") as result_file:
        for line in f:
            parts =  line.strip().split()
            print(parts)
            for part in parts:
                part = int(part)
                if part != 0:
                    result_file.write(1/part)
                else:
                    raise ZeroDivisionError 
except FileNotFoundError as e:
    print("Error: ", e)