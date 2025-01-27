'''
Read multiple lines of text from the user and store it in a file called “INPUT.txt”. Read each character one by one from the file and store vowel characters in "VOWEL.txt" and consonant in "CONSONANT.txt". Print all the file contents.
'''
# Writing user input in INPUT.txt file
def user_input_to_file():
    with open('INPUT.txt','w') as input_file:
        print('Enter text here and write "END" in new line to finish')
        while True :
            line=input()
            if line =="END":
                break
            input_file.write(line+'\n')
# Separating letters as Vowel and Consonent and save it in VOWEL.txt and CONSONENT.txt respt.
def separate_vowel_consonent():
    vowel='AEIOUaeiou'
    with open('INPUT.txt','r') as input_file,\
         open('VOWEL.txt','w') as vowel_file,\
         open('CONSONENT.txt','w') as consonent_file:
        for line in input_file:
            for char in line:
                if char in vowel:
                    vowel_file.write(char)
                else:
                    consonent_file.write(char)
# Read the content from file INPUT.txt , VOWEL.txt and CONSONENT.txt
def print_file_content():
    print('Content of File : INPUT.txt')
    with open('INPUT.txt','r') as input_file:
        print(input_file.read())
    print('Content of File : VOWEL.txt')
    with open('VOWEL.txt','r') as vowel_file:
        print(vowel_file.read())
    print('Content of File : CONSONENT.txt')
    with open('CONSONENT.txt','r') as consonent_file:
        print(consonent_file.read())
# main function
def main():
    user_input_to_file()
    separate_vowel_consonent()
    print_file_content()
if __name__=='__main__':
    main()
