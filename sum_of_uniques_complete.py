#Sum of Unique Elements
def sumOfUnique(nums):
    '''
    copy_nums = nums.copy()
    for item in nums:
        if nums.count(item) > 1: copy_nums.remove(item)
    return sum(copy_nums)
    '''
    #Optimised solution
    unique_nums = [item for item in nums if nums.count(item) == 1]
    return sum(unique_nums)

print(sumOfUnique([1,2,3,2]))