# quick sort
> this is another sorting algorithm employing divide and conquer to achieve sorting.It proves efficient for larger arrays as it just reordersthe existing array instead of creating a new array
## intuition
> by picking an element and reordering the elements in such a way that lesser value elements are before it and grater value elements after it,then that element(pivot) is in it's appropiate posotion in the final sorted array.doing sufficient times sorts the whole array
## solution
- if the list is empty or has just one element,return it is is already sorted
- pick a random element(for my case the last element) from the list.this element is called a pivot
- reorder the list so that all elements with values less than or equal to the pivot come before the pivot while all the elements with values grater than the pivot comes after it.this operation is called partititoning
- the pivot element divides the array into two parts which can be sorted indipendently by making a recursive call to  quick sort.
