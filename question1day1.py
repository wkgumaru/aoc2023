# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from string import digits
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
    print("question 1's answer is: ",sum)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
def question2():
    f = open("testfile.txt", "r")  # opens text file
    Lines = f.readlines()
    newStringArray1 = []
    for newString in Lines:
        if "one" in newString:
            newString = newString.replace("one", "1")
        if "two" in newString:
            newString = newString.replace("two", "2")
        if "three" in newString:
            newString = newString.replace("three", "3")
        if "four" in newString:
            newString = newString.replace("four","4")
        if "five" in newString:
            newString = newString.replace("five", "5")
        if "six" in newString:
            newString = newString.replace("six","6")
        if "seven" in newString:
            newString = newString.replace("seven", "7")
        if "eight" in newString:
            newString = newString.replace("eight", "8")
        if "nine" in newString:
            newString = newString.replace("nine", "9")
        newStringArray1.append(newString)
    sum = 0  # sum to add later
    for newString in newStringArray1:

        number = ""
        for char in newString:
            if char.isdigit():
                number += char
        #print(number)
        lenNumber = len(number)
        if lenNumber > 2:
            number = number[0] + number[-1]
        elif lenNumber == 1:
            number = number[0] + number[0]
        print(number)
        sum += int(number)
    print(sum)

question2()