import os
import re
from datetime import date


# =========================
# 1. File and Directory Operations
# =========================

DIRECTORY_NAME = "classes"
TODAY_FILE_NAME = "today.txt"
NUMBERS_FILE_NAME = "numbers.txt"
EVEN_NUMBERS_FILE_NAME = "even_numbers.txt"
ODD_NUMBERS_FILE_NAME = "odd_numbers.txt"


if not os.path.exists(DIRECTORY_NAME):
    os.makedirs(DIRECTORY_NAME)

with open(TODAY_FILE_NAME, "w") as today_file:
    today_file.write(str(date.today()))

destination_today_path = os.path.join(DIRECTORY_NAME, TODAY_FILE_NAME)
if os.path.exists(destination_today_path):
    os.remove(destination_today_path)

os.rename(TODAY_FILE_NAME, destination_today_path)

numbers = list(range(1, 16))

numbers_file_path = os.path.join(DIRECTORY_NAME, NUMBERS_FILE_NAME)
with open(numbers_file_path, "a") as numbers_file:
    for number in numbers:
        numbers_file.write(f"{number}\n")

even_numbers_file_path = os.path.join(DIRECTORY_NAME, EVEN_NUMBERS_FILE_NAME)
with open(even_numbers_file_path, "w") as even_file:
    for number in numbers:
        if number % 2 == 0:
            even_file.write(f"{number}\n")

odd_numbers_file_path = os.path.join(DIRECTORY_NAME, ODD_NUMBERS_FILE_NAME)
with open(odd_numbers_file_path, "w") as odd_file:
    for number in numbers:
        if number % 2 != 0:
            odd_file.write(f"{number}\n")

for file_name in os.listdir(DIRECTORY_NAME):
    if file_name.endswith(".txt"):
        print(file_name)


# =========================
# 2. Word Occurrence Counter
# =========================

def count_occurrences(file_path: str) -> dict[str, int]:
    word_count: dict[str, int] = {}

    with open(file_path, "r") as text_file:
        for line in text_file:
            words = re.findall(r"\b\w+\b", line)
            for word in words:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1

    return word_count


print(count_occurrences("count_occurrences_EXAMPLE.txt"))