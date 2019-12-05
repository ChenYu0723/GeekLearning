# -*- coding: utf-8 -*-
# @Time    : 2019/12/4 20:58
# @Author  : Chen Yu

# remove-duplicates-from-sorted-array


class Solution:
    def removeDuplicates(self, nums):
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                if nums[j] == nums[i]:
                    nums.pop(j)
                    i -= 1
                    break
                else:
                    break
            i += 1
        return len(nums)


nums = [0,0,1,1,1,2,2,3,3,4]
# print(nums)
print(Solution().removeDuplicates(nums))