# Verify with kavitha mataji
# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. Go to the editor
# Sample List : ['abc', 'xyz', 'aba', '1221']
# Expected Result : 2
def match_words(input_List):
    ctr=0
    for word in input_List:
        if(len(word)>1) & (word[0] == word[-1]):
            ctr += 1
    return ctr
input_List=['abc', 'xyz', 'aba', '1221','abcda']            
print(match_words(input_List))

