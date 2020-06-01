#Bubble Sort 冒泡排序
def bubble(arr):
	n = len(arr)
	for i in range(n):
		already_sorted = True
		for j in range(n-i-1):
			if arr[j] > arr[j+1]:
				arr[j],arr[j+1] = arr[j+1],arr[j]
				already_sorted = False
		if already_sorted:
			break
	return arr


#Insertion Sort 插入排序
def insertion(arr):

	for i in range(1,len(arr)):
		key_item = arr[i]

		j = i - 1

		while j >= 0 and arr[j] > key_item:
			arr[j+1] = arr[j]

			j -= 1
		arr[j+1] = key_item


	return arr

#Merge Sort 合并排序
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

#quicksort 快排
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


test = [1,3,5,2,9,4,1]
print(bubble(test))
print(insertion(test))
print(merge_sort(test))
print(quicksort(test))
