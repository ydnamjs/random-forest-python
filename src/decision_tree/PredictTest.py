from decision_tree.Predict import Predict
from decision_tree._DecisionTree import TreeNode

SUCCESS_COLOR = "\033[92m"
FAIL_COLOR = "\033[91m"
NORM_COLOR = "\033[0m"

def TestPredict()->bool:
    testSuitePassed = True

    testSuitePassed = TestSplitAttributeNotFound() and testSuitePassed
    testSuitePassed = TestLeafNode() and testSuitePassed
    testSuitePassed = TestTwoLayers() and testSuitePassed
    testSuitePassed = TestThreeLayers() and testSuitePassed
    testSuitePassed = TestUnclassifiedSplit() and testSuitePassed

    if testSuitePassed:
        print(f"{SUCCESS_COLOR}TEST SUITE PASSED: PREDICT" + NORM_COLOR)
    else:
        print(f"{FAIL_COLOR}TEST SUITE FAILED: PREDICT" + NORM_COLOR)

    return testSuitePassed

def TestSplitAttributeNotFound()->bool:

    leafNode1 = TreeNode("none", {}, 1)
    leafNode2 = TreeNode("none", {}, 2)
    parentNode = TreeNode("numBooks", {0: leafNode1, 1: leafNode2}, 1)
    row = {"num": 0}

    errorRaised = False

    try:
        Predict(row, parentNode)
    except ValueError:
        errorRaised = True

    if(errorRaised):
        return True

    print(f"{FAIL_COLOR}TEST FAILED: TREE SPLIT ATTRIBUTE NOT IN DATA: expected ValueError to be raised" + NORM_COLOR)
    return False

def TestLeafNode()->bool:

    expected = 0

    leafNode1 = TreeNode("none", {}, 0)
    row = {"numBooks": 3}
    result = Predict(row, leafNode1)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: LEAF NODE: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True

def TestTwoLayers()->bool:

    expected = 1

    leafNode1 = TreeNode("none", {}, 1)
    leafNode2 = TreeNode("none", {}, 2)
    parentNode = TreeNode("numBooks", {0: leafNode1, 1: leafNode2}, 1)
    row = {"numBooks": 0}
    result = Predict(row, parentNode)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: TWO LAYER TREE: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True

def TestThreeLayers()->bool:

    expected = 2

    row = {"numBooks": 1, "numPets": 3}

    leafNode0 = TreeNode("none", {}, 0)
    leafNode1 = TreeNode("none", {}, 1)
    leafNode2 = TreeNode("none", {}, 2)
    parentNode1 = TreeNode("numPets", {2: leafNode0, 3: leafNode2, 1: leafNode1}, 5)
    leafNode3 = TreeNode("none", {}, 3)
    leafNode4 = TreeNode("none", {}, 4)
    parentNode2 = TreeNode("numPets", {3: leafNode3, 2:leafNode4}, 6)
    rootNode = TreeNode("numBooks", {1: parentNode1, 2: parentNode2}, 7)
    result = Predict(row, rootNode)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: THREE LAYER TREE: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True

def TestUnclassifiedSplit()->bool:

    expected = 5

    row = {"numBooks": 1, "numPets": 0}

    leafNode0 = TreeNode("none", {}, 0)
    leafNode1 = TreeNode("none", {}, 1)
    leafNode2 = TreeNode("none", {}, 2)
    parentNode1 = TreeNode("numPets", {2: leafNode0, 3: leafNode2, 1: leafNode1}, 5)
    leafNode3 = TreeNode("none", {}, 3)
    leafNode4 = TreeNode("none", {}, 4)
    parentNode2 = TreeNode("numPets", {3: leafNode3, 2:leafNode4}, 6)
    rootNode = TreeNode("numBooks", {1: parentNode1, 2: parentNode2}, 7)
    result = Predict(row, rootNode)

    if(result != expected):
        print(f"{FAIL_COLOR}TEST FAILED: UNCLASSIFIED SPLIT: expected:" + str(expected) + " recieved: " + str(result) + NORM_COLOR)
        return False

    return True