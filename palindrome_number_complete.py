#9. Palindrome Number
def isPalindrome(input_number):
    input_text = str(input_number)
    if input_text == input_text[::-1]:
        return True
    else:
        return False

print("Enter the number:")
input_num = int(input())
output = isPalindrome(input_num)
print(output)

