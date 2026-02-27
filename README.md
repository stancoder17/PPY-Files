# PPY-Files
Two tasks to practice file management in Python

**Task 1:**
Write code that:
1. Creates a directory named classes.
2. Creates a file named today.txt (in the same path as the classes directory) and writes the execution date to it (use the datetime library).
3. Moves the file today.txt into the classes directory.
4. Creates a list of integers in the range 1–15.
5. Creates a file named numbers.txt inside the classes directory and writes the numbers from the created list to it, each on a new line. If numbers.txt already exists, append the numbers to the existing file without overwriting it.
6. Creates a file named even_numbers.txt containing the even numbers from the previously created list, and a file named odd_numbers.txt containing the odd numbers from that list.
   If these files already exist, their contents should be overwritten.
   Both files must be created inside the classes directory.
7. Displays the contents of the classes directory ["today.txt", "numbers.txt", "odd_numbers.txt", "even_numbers.txt"].
   
Handle cases where files or directories already exist.

**Task 2:**
Write a function count_occurrences(file_path: str) -> dict[str, int] that:
Accepts a path to a .txt file.
Returns a dictionary where the key is a word and the value is the number of occurrences of that word in the given text.
The .txt file will contain a fragment of a book, so punctuation marks must be handled (remove them before counting).
Include proper type hints for both the function argument and the return value.
