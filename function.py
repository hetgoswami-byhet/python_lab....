#1 basic positional argument 
def add(a, b):
    result = a + b
    print(result)
#2 student information 
def student_info(name, age, course):
    print("Student Name:", name)
    print("Student Age:", age)
    print("Course:", course)

student_info("Rahul", 18, "BSc IT")

#3 simple interest 

def simple_interest(p, r, t):
    si = (p * r * t) / 100
    print("Simple Interest =", si)

simple_interest(1000, 5, 2)


#4 area of circle 
def area_circle(r):
    area = 3.14 * r * r
    print("Area of Circle =", area)

area_circle(5)

#5 Chek num positive negative or zero
def check_number(n):
    if n > 0:
        print("Positive number")
    elif n < 0:
        print("Negative number")
    else:
        print("Zero")

check_number(5)

#6 odd or even 
def check_even_odd(n):
    if n % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

check_even_odd(6)

#7 arithmetic sub 

def subtraction(a, b):
    result = a - b
    print("Subtraction =", result)

subtraction(10, 4)