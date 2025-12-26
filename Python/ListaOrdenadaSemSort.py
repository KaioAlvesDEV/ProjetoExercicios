nums = [int(input(f'Digite o {i}nd valor: ')) for i in range(1, 6)]

for i, num in enumerate(nums):
    for j in range(0, len(nums) - 1):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)
