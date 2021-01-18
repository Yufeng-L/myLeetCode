a = [1,5,5,11,16,19,23,65,123,523,523,523,534,799]
#二分搜索法
def binarySearch(nums, target):
	left, right = 0, len(nums) - 1
	while(left <= right):
		mid = left + (right - left) // 2
		if nums[mid] == target:
			return mid
		elif nums[mid] < target:
			left = mid + 1
		elif nums[mid] > target:
			right = mid -1
	return -1

print(binarySearch(a, 9))

#二分搜索左边界
def leftBound(nums, target):
	left, right = 0, len(nums) - 1
	while(left <= right):
		mid = left + (right - left) // 2
		if nums[mid] < target:
			left = mid + 1
		elif nums[mid] > target:
			right = mid - 1
		elif nums[mid] == target:
			right = mid - 1
	# if left >= len(a) or nums[left] != target:
	# 	return -1
	# return left 
	return -1 if left >= len(a) or nums[left] != target else left

print(leftBound(a, 5))

#二分搜索右边界
def rightBound(nums, target):
	left, right = 0, len(nums) - 1
	while(left <= right):
		mid = left + (right - left) // 2
		if nums[mid] < target:
			left = mid + 1
		elif nums[mid] > target:
			right = mid - 1
		elif nums[mid] == target:
			left = mid + 1

	# if right < 0 or nums[right] != target:
	# 	return -1
	# return right
	return -1 if right < 0 or nums[right] != target else right

print(rightBound(a, 523))

















