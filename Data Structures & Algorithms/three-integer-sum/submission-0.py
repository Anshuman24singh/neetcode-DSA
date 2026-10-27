class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        used_first = set()
        n = len(nums)

        for i in range(n - 2):
            if nums[i] in used_first:
                continue
            used_first.add(nums[i])

            seen = set()
            for j in range(i + 1, n):
                third = -(nums[i] + nums[j])
                if third in seen:
                    a = min(nums[i], nums[j], third)
                    c = max(nums[i], nums[j], third)
                    res.add((a, -a - c, c))
                seen.add(nums[j])

        return [list(t) for t in res]                   