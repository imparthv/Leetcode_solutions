#Count the Digits That Divide a Number
def countDigits(num):
    count = 0
    for item in str(num):
        if num % int(item) == 0: count += 1
    return count

print("Enter the number:")
input_num = int(input())
print(countDigits(input_num))