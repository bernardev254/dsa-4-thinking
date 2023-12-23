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
def evaluate_test(func,tests):
    import time
    passed = failed = 0
    total = len(tests)
    for index,test in enumerate(tests):
        start_time = time.time()
        result = func(**test["inputs"])
        time_taken =time.time() - start_time

        print()
        print("Test {}".format(index + 1))
        print("*"*40)
        print()
        if result == test["outputs"]:
            print("Results: PASSED")
            passed += 1
        else:
            print("Results: FAILED")
            failed += 1
       #print("*"*20)
        print(f"Expected Result: {result}")
        print()
        print("Actual Result: {}".format(test["outputs"]))
        print()
        print("Time taken: {:4f}".format(time_taken))
    print()
    print("*"*25)
    print("{}/{} PASSED, {}/{} FAILED".format(passed,total,failed,total))

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
