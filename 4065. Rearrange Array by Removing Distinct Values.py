class Solution(object):
    def rearrangeArray(self, nums):
        ans = []

        while nums:
            nums.sort()

            for i in range(len(nums)):
                if i == 0 or nums[i] != nums[i - 1]:
                    ans.append(nums[i])

            for x in set(nums):
                nums.remove(x)

        return ans
