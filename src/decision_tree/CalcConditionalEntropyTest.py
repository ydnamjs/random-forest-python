from decision_tree.CalcConditionalEntropy import calcConditionalEntropy
import math

SUCCESS_COLOR = "\033[92m"
FAIL_COLOR = "\033[91m"
NORM_COLOR = "\033[0m"

def TestCalcConditionalEntropy()->bool:

    testSuitePassed = True

    testSuitePassed = TestSingleValue() and testSuitePassed
    testSuitePassed = TestMultipleValue() and testSuitePassed
    testSuitePassed = TestManyValue() and testSuitePassed

    if testSuitePassed:
        print(f"{SUCCESS_COLOR}TEST SUITE PASSED: CALC CONDITIONAL ENTROPY" + NORM_COLOR)
    else:
        print(f"{FAIL_COLOR}TEST SUITE FAILED: CALC CONDITIONAL ENTROPY" + NORM_COLOR)
    
    return testSuitePassed

def TestSingleValue()->bool:

    expected = -1 * ((4/17) * math.log2(4/17) + (13/17) * math.log2(13/17))

    valueLabelDicts = []
    valueLabelDicts.append({0: 4, 1: 13})
    result = calcConditionalEntropy(valueLabelDicts)

    if(not (math.isclose(result, expected))):
        print(f"{FAIL_COLOR}TEST FAILED: SINGLE VALUE: expected: " + str(expected) + " recieved: " + str(result)  + NORM_COLOR)
        return False

    return True


def TestMultipleValue()->bool:

    expected = ((-4 / 6) * (1 * math.log2(1) + 0)) + (-2 / 6) * (.5 * math.log2(.5) + .5 * math.log2(.5))

    valueLabelDicts = []
    valueLabelDicts.append({0: 0, 1: 4})
    valueLabelDicts.append({0: 1, 1: 1})
    result = calcConditionalEntropy(valueLabelDicts)

    if(not (math.isclose(result, expected))):
        print(f"{FAIL_COLOR}TEST FAILED: TWO VALUES TWO CLASSES: expected: " + str(expected) + " recieved: " + str(result)  + NORM_COLOR)
        return False

    return True

def TestManyValue()->bool:

    value1Entropy = (-6/14) * (3/6 * math.log2(3/6) + 3/6 * math.log2(3/6))
    value2Entropy = (-4/14) * (1/4 * math.log2(1/4) + 1/4 * math.log2(1/4) + 1/4 * math.log2(1/4) + 1/4 * math.log2(1/4))
    value3Entropy = (-4/14) * (3/4 * math.log2(3/4) + 1/4 * math.log2(1/4))
    expected3 = value1Entropy + value2Entropy + value3Entropy

    valueLabelDicts3 = []
    valueLabelDicts3.append({0: 3, 1: 3})
    valueLabelDicts3.append({1: 1, 2: 1, 3: 1, 4: 1})
    valueLabelDicts3.append({4: 3, 3: 1})

    result3 = calcConditionalEntropy(valueLabelDicts3)

    if(not (math.isclose(result3, expected3))):
        print(f"{FAIL_COLOR}TEST FAILED: MULTIPLE VALUES AND MULTIPLE CLASSES: expected: " + str(expected3) + " recieved: " + str(result3)  + NORM_COLOR)
        return False

    return True