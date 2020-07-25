#Bubble Sort 冒泡排序(稳定)
def bubble(arr):
	n = len(arr)
	for i in range(n-1):
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				already_sorted = False
	return arr

#Insertion Sort 插入排序(稳定)
def insertion(arr):
	for i in range(1,len(arr)):
		key = arr[i]
		j = i - 1
		while j >= 0 and key < arr[j]:
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key
	return arr

#Merge Sort 合并排序(稳定)
def merge(left,right):

	if len(left) == 0:
		return right

	if len(right) == 0:
		return left

	result = []
	index_left = index_right = 0

	while len(result) < len(left) + len(right):
		if left[index_left] <= right[index_right]:
			result.append(left[index_left])
			index_left += 1
		else:
			result.append(right[index_right])
			index_right += 1

		if index_right == len(right):
			result += left[index_left:]
			break

		if index_left == len(left):
			result += right[index_right:]
			break

	return result

def merge_sort(arr):
	if len(arr) < 2:
		return arr

	midpoint = len(arr) // 2

	return merge(left=merge_sort(arr[:midpoint]),\
		right=merge_sort(arr[midpoint:]))

#quicksort 快排(不稳定)
from random import randint
def quicksort(arr):
	if len(arr) < 2:
		return arr

	low, same, high = [],[],[]

	pivot = arr[randint(0,len(arr)-1)]

	for item in arr:

		if item < pivot:
			low.append(item)
		elif item == pivot:
			same.append(item)
		elif item > pivot:
			high.append(item)

	return quicksort(low) + same + quicksort(high)


test = [12,11,13,5,6]
# print(bubble(test))
print(insertion(test))
# print(merge_sort(test))
# print(quicksort(test))
