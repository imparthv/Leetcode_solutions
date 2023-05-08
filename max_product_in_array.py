#Maximum Product of Two Elements in an Array
def maxProduct(nums):
    max_value = 0
    for i in range(0, len(nums)):
        for j in range(1, len(nums)):
            if i != j and ((nums[i] - 1) * (nums[j] - 1)) > max_value: 
                max_value = ((nums[i] - 1) * (nums[j] - 1))
    return max_value

print(maxProduct([3,7]))