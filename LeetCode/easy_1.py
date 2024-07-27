def twoSum(nums: list, target: int) -> list:
    nums2 = nums.copy()
    for ind, num in enumerate(nums):
        second_num = target-num
        nums2.pop(nums2.index(num))
        if (second_num == (target / 2)) and second_num in nums2:
            return [ind, nums2.index(second_num) + ind + 1]
        if second_num in nums2:
            return [ind, nums.index(second_num)]
    

nums = [2,5,5,11]

print(twoSum(nums=nums, target=10))