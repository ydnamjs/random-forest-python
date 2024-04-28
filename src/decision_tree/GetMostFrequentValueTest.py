from decision_tree.GetMostFrequentValue import GetMostFrequentValue

SUCCESS_COLOR = "\033[92m"
FAIL_COLOR = "\033[91m"
NORM_COLOR = "\033[0m"

def TestGetMostFrequentValue()->bool:
    testSuitePassed = True

    testSuitePassed = TestNoData() and testSuitePassed
    testSuitePassed = TestSingleRow() and testSuitePassed
    testSuitePassed = TestManyLabels() and testSuitePassed
    testSuitePassed = TestSameFrequency() and testSuitePassed

    if testSuitePassed:
        print(f"{SUCCESS_COLOR}TEST SUITE PASSED: GET MOST FREQUENT VALUE" + NORM_COLOR)
    else:
        print(f"{FAIL_COLOR}TEST SUITE FAILED: GET MOST FREQUENT VALUE" + NORM_COLOR)

    return testSuitePassed

def TestNoData()->bool:
    """Should raise a value error if there are no rows"""
    data = []

    errorRaised = False

    try:
        GetMostFrequentValue(data)
    except ValueError:
        errorRaised = True

    if(errorRaised):
        return True

    print(f"{FAIL_COLOR}TEST FAILED: NO DATA: expected ValueError to be raised" + NORM_COLOR)
    return False

def TestSingleRow()->bool:
    """Should return the only label when there is 1 entry"""

    expected = 1

    labels = [1]
    result = GetMostFrequentValue(labels)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: SINGLE ROW: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True

def TestManyLabels()->bool:
    """Should return the most frequent label when multiple labels are present regardless of order"""

    expected = 3

    labels = [1, 1, 3, 3, 3, 3, 3, 2, 2, 2]
    result = GetMostFrequentValue(labels)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: MANY LABELS: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True


def TestSameFrequency()->bool:
    """Should return the first encountered label that shares the highest frequency"""

    expected = 3

    labels = [1, 3, 3, 5, 5]
    result = GetMostFrequentValue(labels)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: SAME FREQUENCY: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True