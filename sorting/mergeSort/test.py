def evaluate_test(func,tests):
    import time
    passed = failed = 0
    total = len(tests)
    for index,test in enumerate(tests):
        start_time = time.time()
        result = func(test["inputs"])
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
tests = [
    {
        "inputs":[4,2,6,3,4,6,2,1],
        "outputs":[1,2,2,3,4,4,6,6]
    },
    {
        "inputs":[5,2,6,1,23,7,-12,12,-243,0],
        "outputs":[-243,-12,0,1,2,5,6,7,12,23]
    },
    {
        "inputs":[3,5,6,8,9,10,99],
        "outputs":[3,5,6,8,9,10,99]
    },
    {
        "inputs":[99,10,9,8,6,5,3],
        "outputs":[3,5,6,8,9,10,99]
    },
    {
        "inputs":[5,-12,2,6,1,23,7,7,-12,6,12,1,-243,1,0],
        "outputs":[-243,-12,-12,0,1,1,1,2,5,6,6,7,7,12,23]
    },
    {
        "inputs":[],
        "outputs":[]
    },
    {
        "inputs":[23],
        "outputs":[23]
    },
    {
        "inputs":[42,42,42,42,42,42],
        "outputs":[42,42,42,42,42,42]
    }
]
    

