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
lst = [3,4,7,89,6]
lst1 = [1,3,5,874,2,6,34,53,6,63,85,4,77,5,3,45,3,66,2,45,678,43,32,3,67,85,16,845,7,3,3,78,89,943]
print(merge_sort(lst1))
