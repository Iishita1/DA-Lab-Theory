#Basic Operations
import numpy as np

arr1 = np.array([2,4,6,8])
print(f"Addition: {arr1+2}")
print(f"Multiplication: {arr1*2}")
print(f"Mean of elements of Array: {arr1.mean()}")
print(f"Sum of Elements: {arr1.sum()}")

a=np.array([1,2,3])
b=np.array([4,5,6])
print(f"Addition of two arrays: {a+b}")
print(f"Multiplication of two arrays: {a*b}")
print(f"mean of Array a: {np.mean(a)}")

#Slicing

arr2=np.array([2,4,6,8])
print(f"First two Elements: {arr2[:2]}")