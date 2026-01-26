nums=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
if 3 in nums:
    index = nums.index(3)
    nums[nums.index(3)]=30
print(nums)