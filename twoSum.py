def twoSum(nums, target):
    seen = {}  # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []  # không có lời giải (theo đề bài sẽ không xảy ra)


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  