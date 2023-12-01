# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


f = open("testfile.txt", "r")
Lines = f.readlines()
sum = 0
for line in Lines:
    number = ""
    for char in line:
        if char.isdigit():
            number += char
    if len(number) > 2:
        number = number[0]+number[-1]
    elif len(number) == 1:
        number = number[0]+number[0]
    print(number)
    sum += int(number)
print(sum)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
