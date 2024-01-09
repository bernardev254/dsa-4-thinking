from test import evaluate_test,tests
def merge_sort(nums):
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2
    left,right = nums[:mid], nums[mid:]
    left_sorted, right_sorted = merge_sort(left), merge_sort(right)
    return merge(left_sorted, right_sorted)

def merge(nums1, nums2):
    merged = []
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1
    return merged + nums1[i:] + nums2[j:]

evaluate_test(merge_sort,tests)
