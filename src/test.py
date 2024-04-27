from decision_tree.CalcConditionalEntropyTest import testCalcConditionalEntropy

def testAll()->bool:
    allTestsPassed = True
    
    allTestsPassed = allTestsPassed and testCalcConditionalEntropy()

    if allTestsPassed:
        print("ALL TESTS PASSED")
    return allTestsPassed

testAll()