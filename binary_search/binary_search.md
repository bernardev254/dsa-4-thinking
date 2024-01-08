#  Binary search
## Question
> given a sorted array of integers and a target value, return the index of the target value.
## signature
```
    def search_index(array, target)
        return index
```
- **array :** sorted array from which we are to find the index of the target element
- **target:** integer element that we re finding it's index
- **index:** the position of the element in the array(zero based)

##  some edge cases
1. the element exists at the middle of the array
2. the target exists at the biggining of the array
3. the target element exists at the end of the array
4. the element dosent exists in the array
5. the array is empty

## bruteforce solution
- create a variable named position and initiate it to zero
- iterate through the array 
- compare each element with the target value
- if the target value  equals the element at index position return the position else increment the position and continue to the next element in the array

>**The complexity is in the order of N thus not efficient for large arrays**

## binary search solution
### intuition
> Since the array is sorted then we can reduce the search space by eliminating the elements that are either smaller or larger than our target value.
> we can  access the middle element of the list and compare it with our target value.if the target value is less than the middle element, then we can search the first half of the array and if it's larger then we can search the second half of the array.if equal then we have already found it thus can return it's index
## solution
- create two variables start and end to store the index of the search space.initialize them with zero and length of the array -1 respectively.
- create a while loop  that runs as long as the search space has atleast on value ie(start<=end)
- inside the loop create a variable named mid to store the  index of the middle element,we can initialize it ti (start + end)// 2
- compare the mid element with the target value .if equal return mid as the index,if target is less than the mid element then we adjust the search space(end = mid -1).else if target is larger than then set start = mid + 1.else return -1

