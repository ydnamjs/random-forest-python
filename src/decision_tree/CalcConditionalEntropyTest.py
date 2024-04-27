from decision_tree.CalcConditionalEntropy import calcConditionalEntropy
import math

def testCalcConditionalEntropy()->bool:
    testSuitePassed = True

    testSuitePassed = testSuitePassed and testSingleValue()
    testSuitePassed = testSuitePassed and testMultipleValue()
    testSuitePassed = testSuitePassed and testManyValue()

    if not testSuitePassed:
        print("TEST SUITE FAILED: CALC-ENTROPY")
    return testSuitePassed

def testSingleValue()->bool:
    valueLabelDicts = []
    valueLabelDicts.append({0: 4, 1: 13})
    result = calcConditionalEntropy(valueLabelDicts)
    expected = -1.0 * ((4.0/17) * math.log2(4.0/17) + (13.0/17) * math.log2(13.0/17))

    if(not (math.isclose(result, expected))):
        print("TEST FAILED: CALC-ENTROPY 2: SINGLE VALUE expected: " + str(expected) + " recieved: " + str(result))
        return False

    return True


def testMultipleValue()->bool:
    valueLabelDicts = []
    valueLabelDicts.append({0: 0, 1: 4})
    valueLabelDicts.append({0: 1, 1: 1})
    result = calcConditionalEntropy(valueLabelDicts)
    expected = ((-4.0 / 6.0) * (1 * math.log2(1) + 0)) + (-2.0 / 6.0) * (.5 * math.log2(.5) + .5 * math.log2(.5))

    if(not (math.isclose(result, expected))):
        print("TEST FAILED: CALC-ENTROPY TWO VALUES TWO CLASSES: expected: " + str(expected) + " recieved: " + str(result))
        return False

    return True

def testManyValue()->bool:
    valueLabelDicts3 = []
    valueLabelDicts3.append({0: 3, 1: 3})
    valueLabelDicts3.append({1: 1, 2: 1, 3: 1, 4: 1})
    valueLabelDicts3.append({4: 3, 3: 1})
    result3 = calcConditionalEntropy(valueLabelDicts3)
    value1Entropy = (-6.0/14.0) * (3.0/6.0 * math.log2(3.0/6.0) + 3.0/6.0 * math.log2(3.0/6.0))
    value2Entropy = (-4.0/14.0) * (1.0/4.0 * math.log2(1.0/4.0) + 1.0/4.0 * math.log2(1.0/4.0) + 1.0/4.0 * math.log2(1.0/4.0) + 1.0/4.0 * math.log2(1.0/4.0))
    value3Entropy = (-4.0/14.0) * (3.0/4.0 * math.log2(3.0/4.0) + 1.0/4.0 * math.log2(1.0/4.0))

    expected3 = value1Entropy + value2Entropy + value3Entropy
    if(not (math.isclose(result3, expected3))):
        print("TEST FAILED: CALC-ENTROPY 3: MULTIPLE VALUES AND MULTIPLE CLASSES expected: " + str(expected3) + " recieved: " + str(result3))
        return False

    return True