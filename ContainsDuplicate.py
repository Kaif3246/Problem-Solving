Intuition:
The brute force approach compares each element with every other element in the array to check for duplicates.
If any duplicates are found, it returns true. 
This approach is straightforward but has a time complexity of O(n^2), making it less efficient for large arrays.

Explanation:
The brute force approach involves comparing each element in the array with every other element to check for duplicates. 
If any duplicates are found, return true, otherwise return false.

Brute Force ---

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

Hash Set ----

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        counter = {}
        for num in nums:
            if num in counter and counter[num] >= 1:
                return True
            counter[num] = counter.get(num, 0) + 1
        return False
