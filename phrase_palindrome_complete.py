#125. Valid Palindrome - Needs to be optimised
def isPalindrome(s):
    input_text = list(s.lower())
    copy_list = [item for item in input_text if item.isalnum != False]
    """ for item in input_text:
        if item.isalnum() != False:
            copy_list.append(item) """
    input_string = "".join(copy_list)
    if input_string == input_string[::-1]:
        return True
    else:
        return False


print("Enter your string:")
input_string = str(input())
print(isPalindrome(input_string))