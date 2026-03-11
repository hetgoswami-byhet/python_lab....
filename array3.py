#1.len()-No. of elements in the array

from array import array
arr=array('i',[1,2,3,4,5])
print(len(arr))

#2.append(x)-Adds an element at the end of the array

from array import array
arr=array('i',[1,2,3,4,5])
arr.append(6)
print(arr)


#3.insert(pos,x)-Inserts an element at the specified position

from array import array
arr=array('i',[1,2,3,4,5])
arr.insert(2,10)
print(arr)


#4.remove(x)-removes the first occurrence of an element in the array

from array import array
arr=array('i',[1,2,3,4,5])
arr.remove(3)
print(arr)


#5.pop()-removes and returns the last element of the array

from array import array
arr=array('i',[1,2,3,4,5])
x=arr.pop()
print("element removed:", x)
print(arr)


#6.index(x)-find index of element in the array

from array import array
arr=array('i',[1,2,3,4,5])
print(arr.index(3))


#7.Count()count occurrence of an element in the array

from array import array 
arr=array('i',[1,2,3,4,5,3,3])
print(arr.count(3))


#8.reverse()-reverses Array

from array import array
arr=array('i',[1,2,3,4,5])
arr.reverse()
print(arr)
