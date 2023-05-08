#Reverse String
def reverseString(s):
    s_reverse = s[::-1]
    print(s_reverse)
    print(s.reverse())
#Leetcode solution accepts only s.reverse()

print("Enter string:")
s_string = str(input())
s_list = [s_char for s_char in s_string]
reverseString(s_list)