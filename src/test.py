from decision_tree.CalcConditionalEntropyTest import testCalcConditionalEntropy
from decision_tree.GetMostFrequentValueTest import testGetMostFrequentValue

SUCCESS_COLOR = "\033[92m"
NORM_COLOR = "\033[0m"

def testAll()->bool:
    allTestsPassed = True
    
    allTestsPassed = testCalcConditionalEntropy() and allTestsPassed
    allTestsPassed = testGetMostFrequentValue() and allTestsPassed

    if allTestsPassed:
        print(f"{SUCCESS_COLOR}ALL TESTS PASSED" + NORM_COLOR)
    return allTestsPassed

testAll()