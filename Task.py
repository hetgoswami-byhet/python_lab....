#1 calculate simple intrest
P=float(input("ENTER PRINCIPAL Amount:"))
R=float(input("ENTER RATE OF INTREST"))        
S=float(input("Enter time(in year):"))                
si=(P*R*S)/100
print("simple intrest=",si)
#2 print number 1 to 5
for i in range(1,6):
    print(i)
    #3find maximum number of 2 number
    a=10
    b=25
    print(max(a,b))
    #4find length of string
    my_string="hello,python!"
    length=len(my_string)
    print(length)
    #5
    print("welcome messege")
    #6
    text="sardar narendra modi ki jay"
    print(text[0])
    #7
    text="sardar narendra modi ki jay"
    print(text[-1])
    #8
    n=int(input("enter number:"))
    print(["negative or zero","positive"][n>0])
    #9
    a=1
    b=2
    c=3
    sum=a+b+c
    print("sum =",sum)
    #10
    num=int(input("enter a number:"))
    if num%2==0:
        print(num,"is even")
    else:
        print(num,"is odd")