# insertion sort
> Insertion sort algorithm seeks to sort the initial portion of the list and then inser the other elements into their rightful positions
## insertion sort solution
### intuition
> if we consider the first element of the list alone,then that element is sorted.we can then iterate over the list and for each element place it in its position relative to that sorted portion.
## solution
- iterate over the elements
- pop out the element
- iterate over the element before our element
- insert back the element such that the element before it is smaller and the one after it is larger
