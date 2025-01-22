'''
H. Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing', add 'ly' instead. If the string length
of the given string is less than 3, leave it unchanged.
'''
s=input("Enter the String : ")

if len(s)<3:
    print(s)
elif s.endswith('ing'):
    print(s[0:len(s)-3]+'ly')
else:
    print(s+'ing')

