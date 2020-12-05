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
