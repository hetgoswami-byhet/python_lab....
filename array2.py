#1.Basic slicsing

from array import array
arr=array('i',[1,2,3,4,5])

print(arr[1:4])
print(arr[:3])
print(arr[2:])
print(arr[:])


#2.Slicing with step

from array import array
arr=array('i',[1,2,3,4,5])

print(arr[::2])
print(arr[1::2])
print(arr[::3])


#3.Negative slicing

from array import array
arr=array('i',[1,2,3,4,5])

print(arr[-4:-1])
print(arr[-3:])
print(arr[:-2])


#4.Reverse an array using slicing

from array import array
arr=array('i',[1,2,3,4,5])

print(arr[::-1])


#5.Modify array using slicing

from array import array
arr=array('i',[1,2,3,4,5])

arr[1:4]=array('i',[10,20,30])
print(arr)
