import math

class Point:
    def __init__(self):
        # No-argument constructor that initializes x and y to zero
        self.x = 0
        self.y = 0

    def getinput(self):
        # Get input from the user for x and y
        self.x = float(input("Enter the x-coordinate: "))
        self.y = float(input("Enter the y-coordinate: "))

    def add_point(self, other_point):
        # Add the calling Point object's coordinates with another Point object
        new_point = Point()
        new_point.x = self.x + other_point.x
        new_point.y = self.y + other_point.y
        return new_point

    def diff_point(self, other_point):
        # Calculate the distance between two points
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance

    def display(self):
        # Display the coordinates of the point
        print(f"Point({self.x}, {self.y})")


# Example usage
if __name__ == "__main__":
    point1 = Point()
    point2 = Point()

    print("Enter coordinates for point1:")
    point1.getinput()

    print("Enter coordinates for point2:")
    point2.getinput()

    # Adding two points
    result_point = point1.add_point(point2)
    print("\nAfter adding point1 and point2:")
    result_point.display()

    # Calculating distance between two points
    distance = point1.diff_point(point2)
    print(f"\nDistance between point1 and point2: {distance}")


