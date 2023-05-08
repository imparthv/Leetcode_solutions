#Subtract the Product and Sum of Digits of an Integer
def subtractProductAndSum(n):
    sum = 0
    product = 1
    for item in list(str(n)):
        sum += int(item)
        product = product * int(item)
    return (product - sum)

print("Enter the integer:")
input_n = int(input())

print("The differnece is:", subtractProductAndSum(input_n))
