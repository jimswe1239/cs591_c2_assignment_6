def p4(n):
    """
    param: an integer n
    return: the number of instanes the digit 1 appears in all non-negative numbers that are
    less than or equal to n
    """
    count = 0
    if (n <= 0):
        return count
    else:
        for i in range(1,n+1):
            count = count + str(i).count("1")
    return count
