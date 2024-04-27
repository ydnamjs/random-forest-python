from decision_tree.CalcConditionalEntropyTest import TestCalcConditionalEntropy
from decision_tree.GetMostFrequentValueTest import TestGetMostFrequentValue
from decision_tree.MakeValueLabelDictTest import TestMakeValueLabelDict

SUCCESS_COLOR = "\033[92m"
NORM_COLOR = "\033[0m"

def testAll()->bool:
    allTestsPassed = True
    
    allTestsPassed = TestCalcConditionalEntropy() and allTestsPassed
    allTestsPassed = TestGetMostFrequentValue() and allTestsPassed
    allTestsPassed = TestMakeValueLabelDict() and allTestsPassed

    if allTestsPassed:
        print(f"{SUCCESS_COLOR}ALL TESTS PASSED" + NORM_COLOR)
    return allTestsPassed

testAll()