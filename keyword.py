#1
def simple intrest(p:float,t:float,r:float):
    si=(p*r*t)/100
    print("simple intrest:",si)
 #2   
 def sqr(num,exp=2):
     return num**exp
 print(sqr(3))
 print(sqr(3,3))
 print(sqr(2,4))
 #3
 def add(a,b=5):
     print("sum",a+b)
add(10,20)
add(10)