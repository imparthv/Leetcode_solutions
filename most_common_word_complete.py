#Most Common Word - needs to be optimised
def mostCommonWord(paragraph, banned):
    paragraph = paragraph.lower()
    check_list = []
    word= ""
    count = 0
    for letters in paragraph:
        if letters.isalpha() ==  True or letters == ',' or letters.isspace() == True: 
            word += letters
    check_list = word.split(',')
    word = " ".join(check_list)
    check_list = word.split()
    for item in check_list:
        if check_list.count(item)  > count and item not in banned:
            count = check_list.count(item)
            word = item
    return word
    

           
print("Enter the paragraph:")
input_para = input()
banned_list = []
print("Enter banned:")
ban = input()
banned_list.append(ban)
out_string = mostCommonWord(input_para, banned_list)
print(out_string)
