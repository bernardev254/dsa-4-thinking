from test import evaluate_test
tests = [
  {
   "inputs":{
     "arr":[1,2,3,4,5],
     "target": 3},
    "outputs": 2
  },
  {     
    "inputs":{
     "arr":[2,4,6,8,9],
     "target": 2},
    "outputs": 0
    },
  {
    "inputs":{
     "arr":[4,7,9,12,13,17],
     "target": 17},
    "outputs": 5
    },
  {  
    "inputs":{
     "arr":[],
     "target": 6},
    "outputs": -1
    },
  {    
    "inputs":{
     "arr":[1,2,3,4,5],
     "target": 8},
    "outputs": -1
    }   
    ]


def binary_search(arr, target):
    start, end = 0, len(arr) - 1
    while(start <= end):
        mid = (start + end) // 2
        mid_elem = arr[mid]
        if target == mid_elem:
            return mid
        elif target < mid_elem:
            end = mid -1
        elif target > mid_elem:
            start = mid + 1
    return -1

evaluate_test(binary_search,tests)
