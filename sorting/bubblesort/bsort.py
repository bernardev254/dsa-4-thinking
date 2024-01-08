from test import evaluate_test
tests = [
    {
        
        "inputs": [1,3,2,6,4,8,5,9],
        "outputs": [1,2,3,4,5,6,8,9]
    },
    {
        "inputs": [2,5,7,9,4,2,7],
        "outputs": [2,2,4,5,7,7,9]
    }
]

def bubble_sort(nums):
    nums = list(nums)
    for _ in range(len(nums)-1):
        for elem in range(len(nums)-1):
            if nums[elem] > nums[elem + 1]:
                nums[elem], nums[elem + 1] = nums[elem + 1],nums[elem]
    return nums


evaluate_test(bubble_sort,tests)
