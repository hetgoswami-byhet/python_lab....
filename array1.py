#1.Positional Indexing

from array import array
arr=array('i',[1,2,3,4,5])
print(arr[0]) 
print(arr[2]) 
print(arr[-1]) 


#2.Negative Indexing

from array import array
arr=array('i',[1,2,3,4,5])
print(arr[-1])
print(arr[-3])
print(arr[-5])


#3.modify element in the array

from array import array
arr=array('i',[1,2,3,4,5])
arr[2]=10
print(arr)
