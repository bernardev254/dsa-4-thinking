def insertion(nums):
    nums = list(nums)
    for i in range(len(nums)):
        current = nums.pop(i)
        j = i - 1
        while j >= 0 and nums[j] > current:
            j -= 1
        nums.insert(j + 1, current)
    return nums

list1 = [2,6,9,45,68,3,8,0,65,7,3,4,23,56,8,7,55,64,-23,-345,573]
print(insertion(list1))
