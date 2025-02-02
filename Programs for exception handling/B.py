import csv

class NameErrorException(Exception):
    pass

def create_customer_data():
    # Initialize the nested dictionary for customer details
    customers = {}
    
    n = int(input("Enter the number of customers: "))
    
    for _ in range(n):
        accno = int(input("Enter account number: "))
        name = input("Enter customer name: ")
        balance = float(input("Enter account balance: "))
        customers[accno] = {'name': name, 'balance': balance}
    
    return customers

def process_customers(customers):
    # Initialize the list for storing details of customers with accno <= 100
    customer_list = []
    
    # Open the CSV file for writing
    with open('customers.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Account Number', 'Name', 'Balance'])  # Write header row
        
        for accno, details in customers.items():
            try:
                if accno > 100:
                    # Write customer details to CSV file
                    writer.writerow([accno, details['name'], details['balance']])
                else:
                    # Raise an exception and store details in list
                    raise NameErrorException(f"Account number {accno} is less than or equal to 100.")
            except NameErrorException as e:
                print(e)
                customer_list.append([accno, details['name'], details['balance']])
            finally:
                # Nothing to clean up in this case, so this block is empty
                pass
    
    return customer_list

def print_csv_content(filename):
    with open(filename, mode='r') as file:
        content = file.read()
        print("\nCSV File Content:")
        print(content)

def print_list_content(customer_list):
    print("List of customers with account number <= 100:")
    for customer in customer_list:
        print(customer)

def main():
    customers = create_customer_data()
    customer_list = process_customers(customers)
    
    # Print CSV content and list content
    print_csv_content('customers.csv')
    print_list_content(customer_list)

if __name__ == "__main__":
    main()
