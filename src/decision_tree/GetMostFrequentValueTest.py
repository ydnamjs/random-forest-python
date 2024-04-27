from decision_tree.GetMostFrequentValue import getMostFrequentLabel

SUCCESS_COLOR = "\033[92m"
FAIL_COLOR = "\033[91m"
NORM_COLOR = "\033[0m"

def testGetMostFrequentValue()->bool:
    testSuitePassed = True

    testSuitePassed = testNoData() and testSuitePassed
    testSuitePassed = testSingleRow() and testSuitePassed
    testSuitePassed = testManyLabels() and testSuitePassed
    testSuitePassed = testSameFrequency() and testSuitePassed


    if testSuitePassed:
        print(f"{SUCCESS_COLOR}TEST SUITE PASSED: GET MOST FREQUENT LABEL" + NORM_COLOR)
    else:
        print(f"{FAIL_COLOR}TEST SUITE FAILED: GET MOST FREQUENT LABEL" + NORM_COLOR)

    return testSuitePassed

def testNoData()->bool:
    """Should raise a value error if there are no rows"""
    data = []

    errorRaised = False

    try:
        getMostFrequentLabel(data)
    except ValueError:
        errorRaised = True

    if(errorRaised):
        return True

    print(f"{FAIL_COLOR}TEST FAILED: NO DATA: expected ValueError to be raised" + NORM_COLOR)
    return True

def testSingleRow()->bool:
    """Should return the only label when there is 1 entry"""

    expected = 1

    labels = [1]
    result = getMostFrequentLabel(labels)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: SINGLE ROW: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True

def testManyLabels()->bool:
    """Should return the most frequent label when multiple labels are present regardless of order"""

    expected = 3

    labels = [1, 1, 3, 3, 3, 3, 3, 2, 2, 2]
    result = getMostFrequentLabel(labels)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: MANY LABELS: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True


def testSameFrequency()->bool:
    """Should return the first encountered label that shares the highest frequency"""

    expected = 3

    labels = [1, 3, 3, 5, 5]
    result = getMostFrequentLabel(labels)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: SAME FREQUENCY: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True