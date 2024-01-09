from test import evaluate_test, tests
def quick_sort(nums, start=0, end=None):
    if end is None:
        nums = list(nums)
        end = len(nums) - 1
    if start < end:
        pivot = partition(nums, start, end)
        quick_sort(nums,start,pivot -1)
        quick_sort(nums, pivot + 1, end)
    return nums

def partition(nums, start=0, end=None):
    if end is None:
        end = len(nums) - 1
    
    left_pointer,right_pointer,pivot = start, end - 1, nums[end]
    while right_pointer > left_pointer:
        if nums[left_pointer] <= pivot:
            left_pointer += 1
        elif nums[right_pointer] > pivot:
            right_pointer -= 1
        else:
            nums[left_pointer],nums[right_pointer] = nums[right_pointer], nums[left_pointer]
    if nums[left_pointer] > nums[end]:
        nums[left_pointer],nums[end] = nums[end], nums[left_pointer]
        return left_pointer
    else:
        return end

evaluate_test(quick_sort,tests)

