def problem5(nums):

    numsLen = len(nums)
    count = 0

    #don't include last value since it doesn't have any following values
    for i in range(numsLen - 1):
        
        #only checks values after i
        for j in range(i + 1, numsLen):
            
            if isMoreThan2xGreater(nums[i], nums[j]):
                
                count = count + 1

    return count


def isMoreThan2xGreater(val1, val2):

    if val1 > 2*val2:
        
        return True

    return False
