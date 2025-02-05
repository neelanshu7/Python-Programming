# Base class Publication
class Publication:
    def __init__(self):
        self.title = ""
        self.price = 0.0

    def get(self):
        self.title = input("Enter the title of the publication: ")
        self.price = float(input("Enter the price: "))

    def set(self):
        print(f"Title: {self.title}")
        print(f"Price: ${self.price:.2f}")

# Derived class Book
class Book(Publication):
    def __init__(self):
        super().__init__()
        self.page_count = 0

    def get(self):
        super().get()
        self.page_count = int(input("Enter the number of pages: "))

    def set(self):
        super().set()
        print(f"Page Count: {self.page_count}")

# Derived class Tape
class Tape(Publication):
    def __init__(self):
        super().__init__()
        self.playing_time = 0.0

    def get(self):
        super().get()
        self.playing_time = float(input("Enter the playing time (in minutes): "))

    def set(self):
        super().set()
        print(f"Playing Time: {self.playing_time} minutes")

# Main function to test the classes
def main():
    # Create and test Book instance
    book = Book()
    print("\nEnter details for a book:")
    book.get()
    print("\nBook details:")
    book.set()

    # Create and test Tape instance
    tape = Tape()
    print("\nEnter details for a tape:")
    tape.get()
    print("\nTape details:")
    tape.set()

# Run the main function
if __name__ == "__main__":
    main()
