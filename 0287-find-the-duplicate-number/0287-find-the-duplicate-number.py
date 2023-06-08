class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        firstPointer = 0
        secondPointer = 0
        while (True):
            firstPointer = nums[firstPointer] # -> index = 0 val = 1
            secondPointer = nums[nums[secondPointer]] # -> index = 0 val = 1 -> index = 1 val = 3
            if (firstPointer == secondPointer):
                break
        thirdPointer = 0
        while (True):
            firstPointer = nums[firstPointer]
            thirdPointer = nums[thirdPointer]
            if (firstPointer == thirdPointer):
                return firstPointer