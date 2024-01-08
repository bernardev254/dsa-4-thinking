from test import evaluate_test
tests = [
    {
        "inputs": [1,2,3,4,5,6,7,8],
        "outputs": [2,4,6,8,1,3,5,7]
    },
    {
        "inputs": [3,5,7,9],
        "outputs": [3,5,7,9]
    },
    {
        "inputs": [2,4,6,8,10],
        "outputs": [2,4,6,8,10]
    },
    {
        "inputs": [0,1,2,3,4,5,6,7,8],
        "outputs": [0,2,4,6,8,1,3,5,7]
    },
    {
        "inputs": [],
        "outputs": []
    },
    {
        "inputs": [1,2,4,5,6,6,7,4,2,3],
        "outputs": [2,2,4,4,6,6,1,3,5,7]
    }

]

def sortWithParity(unsorted):
    #sortedList = []
    even = []
    odd = []
    if unsorted is not None:
        for elem in sorted(unsorted):
            if elem == 0:
                even.append(elem)
            elif elem % 2 == 0:
                even.append(elem)
            else:
                odd.append(elem)

    sortedList = even + odd    
    return sortedList

print(evaluate_test(sortWithParity,tests))
