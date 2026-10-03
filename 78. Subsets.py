class Solution(object):
    def subsets(self, nums):

        result = []
        subset = []

        def function(index):

            # Base case
            if index >= len(nums):
                result.append(subset[:])
                return

            # Take
            subset.append(nums[index])
            function(index + 1)

            # Undo
            subset.pop()

            # Don't take
            function(index + 1)

        function(0)

        return result
        
