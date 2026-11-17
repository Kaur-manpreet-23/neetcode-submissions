class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = {}
        a = 0
        for i in nums:
            if (target - i) in arr:
                return [arr[target-i],a]
            arr[i] = a
            a += 1

        