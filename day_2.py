real_count = 0
for line in fileinput.input(files='input.txt'):
    count = 0
    break_line = line.split()
    numbers = break_line[0].split("-")
    letters = break_line[1][:1]
    scrambles = break_line[2]
    for letter in scrambles:
        if letter == letters:
            count += 1
    if count >= int(numbers[0]) and count <= int(numbers[1]):
        real_count += 1
print(real_count)

import fileinput
count = 0
for line in fileinput.input(files='input.txt'):
    break_line = line.split()
    numbers = break_line[0].split("-")
    letters = break_line[1][:1]
    scrambles = break_line[2]
    letter_1 = int(numbers[0]) - 1
    letter_2 = int(numbers[1]) - 1
    print(letter_1, letter_2, letters, scrambles)
    if scrambles[letter_1] != scrambles[letter_2]:
        if scrambles[letter_1] == letters or scrambles[letter_2] == letters:
            count += 1
print(count)
