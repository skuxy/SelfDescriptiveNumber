__author__ = 'skux'


#Solution to problem James Grime has put on his singingbanana Youtube channel
#Not exactly sensible

#prints all self descriptive 10 digit numbers, where 1st digit is number of zeroes in number (0 if there are none,
#which is impossible, but you get the point), 2nd is number of ones, and so on.
#On the hindsight, should have written this one in C or Cpp, executing takes ages


def count(char, string):
    summa = 0
    for e in string:
        if e is char:
            summa += 1
    return summa


def checkDescriptivness(number):
    for index in range(len(number)):
        if count(str(index), number) is not int(number[index]):
            return False
    return True

"""
#Normally you'd need this snipper, but it's paradoxical to have the first digit zero, so I'll take this step down
#in order to speed things up a bit.
def fillNumber(number):
    return number if len(number) == 10 else '0' * (10 - len(number)) + number
"""

#I get memErr, so I'll increment this number in an infinite loop. Sorry.
def main():
    x = 1000000000
    while (True):
        x += 1
        if checkDescriptivness(str(x)):
            print x
            break


if __name__ == "__main__":
    main()