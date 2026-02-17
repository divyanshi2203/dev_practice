class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for i in range(len(nums)):
            other_num = target - nums[i]
            if visited.get(other_num) is not None:
                return [i,visited.get(other_num)]
            visited[nums[i]] = i
                 