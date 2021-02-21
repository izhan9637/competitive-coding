# Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

def findMinHelper(nums, start, end, n):
    # If array consist only one element
    if n == 0:
        return nums[0]
    while start <= end:
        mid = (start + end) // 2

        # There's only one point in the array where this condition is true
        # In our example i.e [4, 5, 6, 7, 0, 1, 2]
        # That point is [7, 0]....because if mid = 3 then nums[mid] > nums[mid+1]
        if nums[mid] > nums[mid+1]:
            # The number of elements before the minimum element in an array is the rotation count
            return nums[mid+1]

        elif nums[mid] < nums[mid+1]:
            # These are two contidions of two halfs of the array
            # For example: [4, 5, 6, 7, 0, 1, 2]
            # Where First Half is [4, 5, 6, 7] and Second Half is [0, 1, 2]

            # Let's say mid = 2 then below condition holds for first half
            if nums[mid] > nums[n]:
                start = mid + 1

            # And if we are in second half then below condition holds true
            # For every element in second half
            elif nums[mid] < nums[n]:
                end = mid - 1

    # This means that array is already sorted and not rotated
    return nums[0]

# arr = [4, 5, 6, 7, 0, 1, 2]
arr = [3,4,5,1,2]
print(findMinHelper(arr, 0, len(arr)-1, len(arr)-1))
