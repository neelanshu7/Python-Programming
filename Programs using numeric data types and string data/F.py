"""
F. Write a Python program that takes a string as input and returns a new string with the
characters reversed. For example, if the input is "python," the output should be "nohtyp."
"""

s=input("Enter your String : ")

s_length=len(s)
print(s_length)

for i in range(len(s)):
    print(s[i],end=' ')
print("\n")
for i in range(len(s)-1,-1 ,-1):
    print(s[i],end=' ')
