#1.print numbers from 1 to 5
for i in range (1,6):
    print(i)

#2.print a message 3 times
for i in range(3):
    print("hello") 

#3.Print number from 1 to 10
for i in range (1,11):
    print(i) 

#4.Print Table of 5
for i in range (1,11):
    print("5x",i,"=",5*i) 

#5.Print Even NUmber from  1 to 20
for i in range(1, 21):
    if i % 2 == 0:
        print(i) 

#6.Print odd numbers from 1 to 15
for i in range(1, 16):
    if i % 2 != 0:
        print(i)


#7.Print characters of a string.
name = "ATMIYA"

for letter in name:
    print(letter)

#8. Sum of NUmbers from from 1 to 5
total = 0
for i in range(1,6):
    total=total + i
    print("sum is:",total)

#9.Print list elements
numbers = [10,20,30,40]

for n in numbers:
    print(n)



