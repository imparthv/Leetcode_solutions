#Add Digits
def addDigits(num):
    if num >= 0 and num <= 9 :
        return num
    
    else:
        count = 0
        num = str(num)
        num_list = [nums for nums in num]
        for item in num_list:
            count+=int(item)
        if count >= 0 and count <= 9:
            return count
        else:
            return addDigits(count)


print("Enter number:")
target = int(input())
output_num = addDigits(target)
print(output_num)