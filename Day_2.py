# class Solution(object):
#     def getConcatenation(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
        
#         return nums+nums


def concatenateArrays(arr1, arr2):
    # Using the + operator to concatenate the arrays
    return arr1 + arr2
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
print("First array:", arr1)
print("Second array:", arr2)
result = concatenateArrays(arr1, arr2)
print("Concatenated array:", result)
