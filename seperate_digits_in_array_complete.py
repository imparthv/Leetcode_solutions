#Separate the Digits in an Array
def separateDigits(nums):
    seperate_list = []
    for item in nums:
        item = str(item)
        for items in item:
            seperate_list.append(int(items))
    return seperate_list

print(separateDigits([13,25,83,77]))