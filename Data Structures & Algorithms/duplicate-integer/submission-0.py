class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set()
        for i in nums:
            old_len = len(nums_set)
            nums_set.add(i)
            if len(nums_set) == old_len:
                return True
        return False