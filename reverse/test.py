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
        print(f"Actual Result: {result}")
        print()
        print("Expected Result: {}".format(test["outputs"]))
        print()
        print("Time taken: {:4f}".format(time_taken))
    print()
    print("*"*25)
    print("{}/{} PASSED, {}/{} FAILED".format(passed,total,failed,total))

