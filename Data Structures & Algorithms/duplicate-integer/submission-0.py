class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        set_nums = set(nums)
        if len(nums) - len(set_nums) > 0:
            return True
        else:
            return False