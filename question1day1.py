# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def question1():
    f = open("testfile.txt", "r")  # opens text file
    Lines = f.readlines()
    sum = 0
    for line in Lines:  # loop through file
        number = ""
        for char in line:
            if char.isdigit():
                number += char
        lenNumber = len(number)
        if lenNumber > 2:
            number = number[0] + number[-1]
        elif lenNumber == 1:
            number = number[0] + number[0]
        sum += int(number)
    print(sum)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
question1()