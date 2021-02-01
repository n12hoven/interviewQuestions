# Interview question Prodigy
# The positive whole numbers up to and including 10
# which are multiplesof 3 or 5 are: 3, 5, 6, 9, 10.
# What is the sum of all positive whole numbers,
# up to and including 1000, which are multiples of 13 or 31?

def thirteen(num):
# for all of 13
    if num % 13 == 0:
        return True
    else:
        return False          

def thirtyone(num):
# for all of 31
    if num % 31 == 0:
        return True
    else:
        return False  


def sumNumbers(maxNum):
# the sum of all divisibles
# of 13 & 31, up to and including
# the int of maxNum
    numArray = []
    sum = 0
    num = 0
    while num <= maxNum:
        if thirteen(num) == True:
            numArray.append(num)
        if thirtyone(num) == True:
            numArray.append(num)
        num += 1
    for i in numArray:
        sum = sum + i
    return sum

print(sumNumbers(int(input("maxNum = "))))
    
