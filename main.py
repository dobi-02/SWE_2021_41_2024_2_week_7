from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    
    indices = {}

    for i, num in enumerate(nums):
        comp = target - num
        if comp in indices:
            return [indices[comp], i]
        indices[num] = i

