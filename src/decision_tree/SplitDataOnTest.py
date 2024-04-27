from decision_tree.SplitDataOn import SplitDataOn

SUCCESS_COLOR = "\033[92m"
FAIL_COLOR = "\033[91m"
NORM_COLOR = "\033[0m"

def TestSplitDataOn()->bool:
    testSuitePassed = True

    testSuitePassed = TestRowsMustHaveSplitAttr() and testSuitePassed
    testSuitePassed = TestSingleAttributeValue() and testSuitePassed
    testSuitePassed = TestManyValuesManyAttr() and testSuitePassed

    if testSuitePassed:
        print(f"{SUCCESS_COLOR}TEST SUITE PASSED: SPLIT DATA ON" + NORM_COLOR)
    else:
        print(f"{FAIL_COLOR}TEST SUITE FAILED: SPLIT DATA ON" + NORM_COLOR)

    return testSuitePassed

def TestRowsMustHaveSplitAttr()->bool:
    """Should raise a value error if we encounter a row that does not have the split attribute"""

    splitAttribute = "numApples"
    trainingData = [
        {"numApples": 3, "numCharacters": 21},
        {"numFruit": 6, "numCharacters": 12},
        {"numApples": 9, "numCharacters": 10}
    ]

    errorRaised = False

    try:
        SplitDataOn(splitAttribute, trainingData)
    except ValueError:
        errorRaised = True

    if(errorRaised):
        return True

    print(f"{FAIL_COLOR}TEST FAILED: MISSING SPLIT ATTRIBUTE: expected ValueError to be raised" + NORM_COLOR)
    return False

def TestSingleAttributeValue()->bool:
    """Should return all data if there is only one value for the attribute being split on"""

    expected = {1: [
        {"numCharacters": 21},
        {"numCharacters": 12},
        {"numCharacters": 10}
    ]}

    splitAttribute = "numApples"
    trainingData = [
        {"numApples": 1, "numCharacters": 21},
        {"numApples": 1, "numCharacters": 12},
        {"numApples": 1, "numCharacters": 10}
    ]
    result = SplitDataOn(splitAttribute, trainingData)

    if result != expected:
        print(f"{FAIL_COLOR}TEST FAILED: SINGLE ATTRIBUTE VALUE: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True

def TestManyValuesManyAttr()->bool:
    """Should return rows of data where each row is in a group based on the split attribute's value"""

    expected = {
        2: [
            {"numCharacters": 17, "numDogs": 0, "numFriends": 5, "class": 0},
            {"numCharacters": 9, "numDogs": 5, "numFriends": 6, "class": 0},
            {"numCharacters": 13, "numDogs": 3, "numFriends": 3, "class": 0},
            {"numCharacters": 2, "numDogs": 0, "numFriends": 4, "class": 0},
            {"numCharacters": 4, "numDogs": 0, "numFriends": 5, "class": 0},
            {"numCharacters": 8, "numDogs": 2, "numFriends": 2, "class": 0},
            {"numCharacters": 2, "numDogs": 7, "numFriends": 6, "class": 0},
        ],
        0: [
            {"numCharacters": 11, "numDogs": 3, "numFriends": 7, "class": 0},
            {"numCharacters": 19, "numDogs": 5, "numFriends": 4, "class": 0},
            {"numCharacters": 16, "numDogs": 3, "numFriends": 5, "class": 0},
        ],
        1: [
            {"numCharacters": 13, "numDogs": 6, "numFriends": 5, "class": 0},
            {"numCharacters": 14, "numDogs": 7, "numFriends": 6, "class": 0},
            {"numCharacters": 15, "numDogs": 23, "numFriends": 7, "class": 0},
            {"numCharacters": 16, "numDogs": 1, "numFriends": 8, "class": 0}
        ],
        3: [
            {"numCharacters": 4, "numDogs": 8, "numFriends": 7, "class": 0},
            {"numCharacters": 5, "numDogs": 2, "numFriends": 3, "class": 0},
            {"numCharacters": 6, "numDogs": 4, "numFriends": 2, "class": 0},
        ]
    }

    splitAttribute = "numApples"
    trainingData = [
        {"numApples": 2, "numCharacters": 17, "numDogs": 0, "numFriends": 5, "class": 0},
        {"numApples": 2, "numCharacters": 9, "numDogs": 5, "numFriends": 6, "class": 0},
        {"numApples": 2, "numCharacters": 13, "numDogs": 3, "numFriends": 3, "class": 0},
        {"numApples": 0, "numCharacters": 11, "numDogs": 3, "numFriends": 7, "class": 0},
        {"numApples": 1, "numCharacters": 13, "numDogs": 6, "numFriends": 5, "class": 0},
        {"numApples": 2, "numCharacters": 2, "numDogs": 0, "numFriends": 4, "class": 0},
        {"numApples": 2, "numCharacters": 4, "numDogs": 0, "numFriends": 5, "class": 0},
        {"numApples": 1, "numCharacters": 14, "numDogs": 7, "numFriends": 6, "class": 0},
        {"numApples": 1, "numCharacters": 15, "numDogs": 23, "numFriends": 7, "class": 0},
        {"numApples": 0, "numCharacters": 19, "numDogs": 5, "numFriends": 4, "class": 0},
        {"numApples": 2, "numCharacters": 8, "numDogs": 2, "numFriends": 2, "class": 0},
        {"numApples": 2, "numCharacters": 2, "numDogs": 7, "numFriends": 6, "class": 0},
        {"numApples": 3, "numCharacters": 4, "numDogs": 8, "numFriends": 7, "class": 0},
        {"numApples": 0, "numCharacters": 16, "numDogs": 3, "numFriends": 5, "class": 0},
        {"numApples": 3, "numCharacters": 5, "numDogs": 2, "numFriends": 3, "class": 0},
        {"numApples": 3, "numCharacters": 6, "numDogs": 4, "numFriends": 2, "class": 0},
        {"numApples": 1, "numCharacters": 16, "numDogs": 1, "numFriends": 8, "class": 0},
    ]
    result = SplitDataOn(splitAttribute, trainingData)

    if result != expected:
        print(f"{FAIL_COLOR}TEST FAILED: MANY VALUES MANY ATTRIBUTES: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True