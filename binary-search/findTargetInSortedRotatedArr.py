def shiftedBinarySearch(array, target):
	return shiftedBinarySearchHelper(array, target, 0, len(array) - 1)

# Iterative Version
# Time: O(log(N)) and Space: O(1)
def shiftedBinarySearchHelper(array, target, left, right):
	while left <= right:
		mid = (left + right) // 2
		potentialMatch = array[mid]
		leftNum = array[left]
		rightNum = array[right]

		if target == potentialMatch:
			print("mid =>",array[mid])
			return mid
		elif leftNum <= potentialMatch:
			if target >= leftNum and target < potentialMatch:
				right = mid - 1
			else:
				left = mid + 1
		else:
			if target > potentialMatch and target <= rightNum:
				left = mid + 1
			else:
				right = mid - 1
	return -1

# Recursive Version
# Time: O(log(N)) and Space: O(log(N))

#def shiftedBinarySearchHelper(array, target, left, right):
#	if left > right:
#		return -1
#
#	mid = (left + right) // 2
#	potentialMatch = array[mid]
#	leftNum = array[left]
#	rightNum = array[right]
#
#	if target == potentialMatch:
#		return mid
#	elif leftNum <= potentialMatch:
#		if target >= leftNum and target < potentialMatch:
#			return shiftedBinarySearchHelper(array, target, left, mid - 1)
#		else:
#			return shiftedBinarySearchHelper(array, target, mid + 1, right)
#	else:
#		if target > potentialMatch and target <= rightNum:
#			return shiftedBinarySearchHelper(array, target, mid + 1, right)
#		else:
#			return shiftedBinarySearchHelper(array, target, left, mid - 1)

if __name__ == "__main__":
	# 33
	arr = [45, 61, 71, 72, 73, 0, 1, 21, 33, 45]
	print(shiftedBinarySearch(arr, 33))
