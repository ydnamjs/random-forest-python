from decision_tree.ExtractFeatureValues import ExtractFeatureValues

SUCCESS_COLOR = "\033[92m"
FAIL_COLOR = "\033[91m"
NORM_COLOR = "\033[0m"

def TestExtractFeatureValues()->bool:
    testSuitePassed = True

    testSuitePassed = TestIncompleteRow() and testSuitePassed
    testSuitePassed = TestNoData() and testSuitePassed
    testSuitePassed = TestSingleRow() and testSuitePassed
    testSuitePassed = TestManyRows() and testSuitePassed

    if testSuitePassed:
        print(f"{SUCCESS_COLOR}TEST SUITE PASSED: EXTRACT FEATURE VALUES" + NORM_COLOR)
    else:
        print(f"{FAIL_COLOR}TEST SUITE FAILED: EXTRACT FEATURE VALUES" + NORM_COLOR)

    return testSuitePassed

def TestIncompleteRow():

    data = [
        {"total_garbage": 3, "num_snakes_owned": 0},
        {"total_garb": 7, "num_snakes_owned": 1},
        {"total_garbage": 2, "num_snakes_owned": 2}
    ]
    featureName = "total_garbage"

    errorRaised = False

    try:
        ExtractFeatureValues(data, featureName)
    except ValueError:
        errorRaised = True

    if(errorRaised):
        return True

    print(f"{FAIL_COLOR}TEST FAILED: INCOMPLETE ROW: expected ValueError to be raised" + NORM_COLOR)
    return False

def TestNoData():
    expected = []

    data = []
    featureName = "total_garbage"
    result = ExtractFeatureValues(data, featureName)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: NO DATA: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True

def TestSingleRow():
    expected = [4]

    data = [
        {"total_garbage": 4},
    ]
    featureName = "total_garbage"
    result = ExtractFeatureValues(data, featureName)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: SINGLE DATA: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True

def TestManyRows():
    expected = [7, 5, 4, 3, 1, 5, 7, 6, 3, 5, 6]

    data = [
        {"total_garbage": 3, "num_snakes": 7, "label": 4, "favorite_food": 6},
        {"total_garbage": 5, "num_snakes": 5, "label": 2, "favorite_food": 3},
        {"total_garbage": 7, "num_snakes": 4, "label": 1, "favorite_food": 4},
        {"total_garbage": 2, "num_snakes": 3, "label": 5, "favorite_food": 2},
        {"num_snakes": 1, "label": 2, "favorite_food": 7, "total_garbage": 1},
        {"num_snakes": 5, "label": 8, "favorite_food": 8, "total_garbage": 4},
        {"num_snakes": 7, "label": 9, "favorite_food": 2, "total_garbage": 5},
        {"favorite_food": 1, "total_garbage": 11, "label": 1, "num_snakes": 6},
        {"favorite_food": 5, "total_garbage": 4, "label": 4, "num_snakes": 3},
        {"favorite_food": 7, "total_garbage": 16, "label": 5, "num_snakes": 5},
        {"favorite_food": 8, "total_garbage": 999, "label": 6, "num_snakes": 6},
    ]
    featureName = "num_snakes"
    result = ExtractFeatureValues(data, featureName)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: SINGLE DATA: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True