#Contains Duplicate
def containsDuplicate(nums):
    temp_nums = nums.copy()
    nums = set(nums)
    if len(nums) < len(temp_nums):return True
    else: return False

input_list = [1,1,1,3,3,4,3,2,4,2]
print(containsDuplicate(input_list))