#Find Lucky Integer in an Array
def findLucky(arr):
    lucky_integer = 0
    for item in arr:
        if arr.count(item) == item and item > lucky_integer:  lucky_integer = item
    if lucky_integer: return lucky_integer
    else: return -1
            

print(findLucky([2,2,2,3,3]))