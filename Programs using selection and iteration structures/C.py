"""
C. Design a program that assesses the strength of a given password based on specific
    criteria and categorizes it as either "Weak," "Moderate," or "Strong."
"""
'''
1.The program should prompt the user to enter a password.
2.The password strength is determined based on the following criteria:
    Length Check:
        The password must be at least 8 characters long.
    Case SensiMvity:
        The password should contain a mix of uppercase and lowercase leaers.
    Numeric Characters:
        The password should include at least one numeric digit.
    Special Characters:
        The password should contain at least one special character from the set: !@#$%^&*(),.?":{}|<>
    Domain Check:
        All the mail ID must be finished with @sastra.ac.in or @sastra.edu
'''

def domain_check(email):
    return email.endswith('sastra.ac.in') or email.endswith('sastra.edu')

def pas_strength(pas):
    if len(pas)<8:
        return 'Weak'

    has_upper=any(c.isupper() for c in pas)
    has_lower=any(c.islower() for c in pas)
    has_digit=any(c.isdigit() for c in pas)
    has_spc_char=any(c in '!@#$%^&*(),.?":{}|<>' for c in pas)

    if has_upper and has_lower and has_digit:
        if has_spc_char:
            return 'Strong'
        else:
            return 'Moderate'
    return 'Weak'
def main():
    email=input("Enter your Email ID : ")

    if not domain_check(email):
        print("Invalid Domain!! Email ID must ends with @sastra.edu or @sastra.ac.in")
        return
    
    pas=input("Enter your Password : ")
    strength=pas_strength(pas)
    print("Your Password Strength is ", strength)

main()
