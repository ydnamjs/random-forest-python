from decision_tree.MakeValueLabelDict import MakeValueLabelDict

SUCCESS_COLOR = "\033[92m"
FAIL_COLOR = "\033[91m"
NORM_COLOR = "\033[0m"

def TestMakeValueLabelDict()->bool:
    testSuitePassed = True

    testSuitePassed = TestDataLenMismatch() and testSuitePassed
    testSuitePassed = TestNoData() and testSuitePassed
    testSuitePassed = TestSinglePair() and testSuitePassed

    if testSuitePassed:
        print(f"{SUCCESS_COLOR}TEST SUITE PASSED: MAKE VALUE LABEL DICT" + NORM_COLOR)
    else:
        print(f"{FAIL_COLOR}TEST SUITE FAILED: MAKE VALUE LABEL DICT" + NORM_COLOR)

    return testSuitePassed

def TestDataLenMismatch()->bool:
    """Should raise a value error if the length of values and labels do not match"""
    values = [1, 2, 3]
    labels = [0, 1]

    errorRaised = False

    try:
        MakeValueLabelDict(values, labels)
    except ValueError:
        errorRaised = True

    if(errorRaised):
        return True

    print(f"{FAIL_COLOR}TEST FAILED: DATA LENGTH MISMATCH: expected ValueError to be raised" + NORM_COLOR)
    return False

def TestNoData()->bool:
    """Should raise a value error if there are no values or labels"""
    values = []
    labels = []

    errorRaised = False

    try:
        MakeValueLabelDict(values, labels)
    except ValueError:
        errorRaised = True

    if(errorRaised):
        return True

    print(f"{FAIL_COLOR}TEST FAILED: NO DATA: expected ValueError to be raised" + NORM_COLOR)
    return False

def TestSinglePair()->bool:
    """A single pair should return a list of valueLabelDictionaries with with a single valueLabelDictionary who has one label that appears once"""

    expected = {}
    labelDict = {}
    labelDict[2] = 1
    expected[0] = labelDict

    values = [0]
    labels = [2]
    result = MakeValueLabelDict(values, labels)

    if result != expected:
        print(f"{FAIL_COLOR}TEST FAILED: SINGLE PAIR: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True