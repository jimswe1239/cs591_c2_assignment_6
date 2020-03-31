import math


def p3(num1, num2):
    """
    Assume input is only ever integers greater than or equal to 0
    """
    product = "0"

    # input strings become array lists
    num1Array = list(num1)
    num2Array = list(num2)

    # number version of input strings
    num1Int = stringToInt(num1Array)
    num2Int = stringToInt(num2Array)

    # find product of two numbers
    productInt = num1Int * num2Int

    # make product into string
    product = intToString(productInt)

    return product


def stringToInt(numArray):

    numInt = 0
    # converting num1 array to integers from left to right
    for i in range(len(numArray)):

        # get the ASCII value of number and subtract 48 to get real value of integer
        numInt += ord(numArray[i]) - 48

        # create a space in the right hand side for the next digit if it exists
        if i != len(numArray) - 1:
            numInt *= 10

    return numInt


# convert integer to string
def intToString(num):
    # boolean to indicate no more digits of number left to convert to string
    nextDigitExists = True
    ret = ""

    while nextDigitExists:
        # take last digit of number
        temp = num % 10

        # make into a character and add to beginning of string
        ret = (chr((temp + 48))) + ret

        # get rid of last digit
        num = math.floor(num / 10)

        # if we are out of digits break out of loop
        if num == 0:
            nextDigitExists = False

    return ret
