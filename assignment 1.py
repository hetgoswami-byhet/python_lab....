
# Q1: Display a welcome message
print("Welcome to Python Programming!")


# Q2: Print address using \t for tab and \n for new line

print("Rajfath Kumar\nFlat No.101,\tSuntlhy Apartment\nII G Road,\tSector-5\nRajkot.\nPincode:\t360004\nIndia.")


# Q3: Perform four basic mathematical operations (150 & 120.50)

a = 150
b = 120.50
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)


# Q4: Calculate area and circumference of circle
#     Area = 3.14 * radius^2
#     Circumference = 2 * 3.14 * radius

radius = float(input("Enter radius: "))
area = 3.14 * radius * radius
circumference = 2 * 3.14 * radius
print("Area of circle:", area)
print("Circumference of circle:", circumference)

# Q5: Calculate Simple Interest
#     SI = (P * R * T) / 100
P = float(input("Enter Principal Amount: "))
R = float(input("Enter Rate of Interest: "))
T = float(input("Enter Time (in years): "))
SI = (P * R * T) / 100
print("Simple Interest:", SI)


# Q6: Calculate perimeter of rectangle
#     Perimeter = 2 * (length + width)
length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = 2 * (length + width)
print("Perimeter of Rectangle:", perimeter)