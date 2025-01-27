import csv

# Function to write student details to Data.csv
def write_student_data_to_csv(students):
    with open("Data.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Rollno", "Name", "Mark1", "Mark2", "Mark3", "Total"])
        for student in students:
            total = student[2] + student[3] + student[4]
            writer.writerow(student + [total])

# Function to extract students with total marks > 250 and write to OUTPUT.csv
def extract():
    with open("Data.csv", "r") as infile, open("OUTPUT.csv", "w", newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(next(reader))  # Write the header
        for row in reader:
            total = int(row[5])  # Total is at the 6th position (index 5)
            if total > 250:
                writer.writerow(row)

# Function to print the contents of a CSV file
def print_csv_file_contents(filename):
    print(f"\nContents of {filename}:")
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

# Main function to execute the tasks
def main():
    # Sample list of students: [Rollno, Name, Mark1, Mark2, Mark3]
    students=[[1,'Ram',80,90,85],
             [2,'Ravi',70,60,50],
             [3,'Rishi',95,85,90],
             [4,'Rohit',65,70,60]]

    write_student_data_to_csv(students)
    extract()
    print_csv_file_contents("Data.csv")
    print_csv_file_contents("OUTPUT.csv")

if __name__ == "__main__":
    main()
