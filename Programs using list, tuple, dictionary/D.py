def input_person_details():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        address = input("Enter your address: ")
        
        # Validate age to ensure it's a positive integer
        if age < 0:
            raise ValueError("Age must be a non-negative integer.")
        
        # Pack the details into a tuple
        person_info = (name, age, address)
        return person_info
    
    except ValueError as e:
        print(f"Error: {e}")
        return None

def display_person_info(person_info):
    if person_info:
        name, age, address = person_info
        print("\nPersonal Information:")
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Address: {address}")
    else:
        print("No information to display.")

def main():
    print("Welcome to the Personal Information Management System")
    
    while True:
        person_info = input_person_details()
        if person_info:
            display_person_info(person_info)
        
        continue_prompt = input("\nDo you want to enter another person's information? (yes/no): ").strip().lower()
        if continue_prompt != 'yes':
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()
