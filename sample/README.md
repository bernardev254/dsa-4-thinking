## Question
> given an integer array `heights`  of length `n`.There are n vertical lines drawn such that the two endpoints of the ith line are (i,0) and (i,height[i]).Find two lines that together with the x-axis form a  container such that the container contains the  most water.Return the maximum ammount of water a container can store interms of area.
## signature
```
    def max_area(heights)
        return max_area
```
- **heights :**  array containing heights of the prospective container walls
- **max_area:** the max rectangular area holding the max water

##  some edge cases
1. 
2. 
## bruteforce solution


## linear solution
### intuition
> we can  can have two walls and compute the area then adjust the short wall in quest for a bigger area.
## solution
- maintain two pointers
- intialize max_area to 0
- while the pointer are further apart,calculate the min height,distance between the two walls and the area(min-height * distance)
- if the area is grater that the max_area then max_area = area
- adjust the pointer such that you advance to a taller wall than the min wall 
- return the max area
