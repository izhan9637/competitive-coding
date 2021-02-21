# Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

def searchForRange(array, target):
	finalRange= [-1, -1]
	findRange(array, target, 0, len(array) - 1, finalRange, True)
	findRange(array, target, 0, len(array) - 1, finalRange, False)
	return finalRange

# Iterative
# Time: O(log(N)) and Space: O(1)
def findRange(array, target, left, right, res, isLeft):
	while left <= right:
		mid = (left + right) // 2

		if array[mid] < target:
			left = mid + 1
		elif array[mid] > target:
			right = mid - 1
		else:
			if isLeft:
				if mid == 0 or array[mid - 1] != target:
					res[0] = mid
					return
				else:
					right = mid - 1
			else:
				if mid == len(array) - 1 or array[mid + 1] != target:
					res[1] = mid
					return
				else:
					left = mid + 1


if __name__ == "__main__":
	arr = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73]
	target = 45
	print(searchForRange(arr, target))


# Recursive
# Time: O(log(N)) and Space: O(log(N)) .. because of call stack
#def findRange(array, target, left, right, res, isLeft):
#	if left > right:
#		return
#
#	mid = (left + right) // 2
#
#	if array[mid] < target:
#		findRange(array, target, mid + 1, right, res, isLeft)
#	elif array[mid] > target:
#		findRange(array, target, left, mid - 1, res, isLeft)
#	else:
#		if isLeft:
#			if mid == 0 or array[mid - 1] != target:
#				res[0] = mid
#			else:
#				findRange(array, target, left, mid - 1, res, isLeft)
#		else:
#			if mid == len(array) - 1 or array[mid + 1] != target:
#				res[1] = mid
#			else:
#				findRange(array, target, mid +1 , right, res, isLeft)
