#Average Value of Even Numbers That Are Divisible by Three
def avaerageValue(nums):
    sum = count = 0
    for num in nums:
        if num % 2 == 0 and num % 3 == 0:
            sum+=num
            count+=1
    if count !=0 : return int(sum/count)
    else: return 0

print(avaerageValue([1,3,6,10,12,15]))