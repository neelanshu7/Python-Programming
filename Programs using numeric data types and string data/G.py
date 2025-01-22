"""
G. Develop a Python function to determine if a given string is a palindrome. Ignore
spaces, punctuation, and capitalization in the comparison.
"""
s=input("Enter string value : ")

print("Input String is : ",end=' ')
for i in range(len(s)):
    print(s[i],end='')

print("\nReversed String is : ",end=' ')
for i in range(len(s)-1,-1,-1):
    print(s[i],end='')

print("\n")

if(s.lower()==s.lower()[::-1]):
    print("String is Palindrome")
else:
    print("String is not a Palindrome")
