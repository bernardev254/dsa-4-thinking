from test import evaluate_test,tests
def max_area(heights):
    indexA,indexB = 0, len(heights) - 1
    maxArea = 0
    while indexB > indexA:
        wall1 = heights[indexA]
        wall2 = heights[indexB]
        shortWall = min(wall1,wall2)
        length = (abs(indexA - indexB))
        area = (shortWall * length)
        #print(f"{shortWall} * {length} = {area}")
        if area > maxArea:
            maxArea = area
        if wall1 == shortWall:
            indexA += 1
        if wall2 == shortWall:
            indexB -= 1
    return maxArea

evaluate_test(max_area,tests)
