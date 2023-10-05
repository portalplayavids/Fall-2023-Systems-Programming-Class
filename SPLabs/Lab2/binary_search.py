#!/usr/bin/env python3
array = [n for n in range(10)]

def binary_search(array, val):
	if array[middle] == val:
		return middle;
	elif array[middle] < val:
		mid = mid + 1;	# left
	elif array[middle] > val:
		mid  = mid - 1; # right
	

print(binary_search(array,3))
print(binary_search(array,7))
print(binary_search(array,11))
print(binary_search(array,20))
