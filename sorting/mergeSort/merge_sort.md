#  merge sort
this is a sorting algorithm  that employs divide and conquer to divide the problem into subproblems,solve them recursively and then combine the outputs
## merge sort solution
### intuition
> if we divide the array into individual elements,then then that is a sortedsingle element array.we can then merge those sorted arrays to get one sorted array.
## solution
- if the input list is empty or contains just one element ,then the array is sorted,return it
- if not divide the list of numbers into two roughly equal parts
- sort each part recursively using the merge sort algorithm you will get back two sorted lists
- merge the two sorted lists to get a single sorted list
