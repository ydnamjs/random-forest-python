from typing import Dict
from math import log2

def calcConditionalEntropy(valueLabelDicts: list[Dict[int, int]])->float:
    """
        @param valueLabelDicts: list of each feature's value classification amounts
        ex: if our feature could be the value 0 or 1 and our label could be 3 or 4 and our data looked like
        0 3; 0 3; 0 4; 1 4; 1 4; 1 3 our valueLabelDicts would be [{3: 2, 4: 1}, {3: 1, 4: 2}] because for value 0, 3 appears twice and 4 appears once

        @returns the entropy of splitting on this feature
    """

    totalInstances = 0
    for value in valueLabelDicts:
        for classAmt in value.values():
            totalInstances += classAmt

    entropy = 0
    for value in valueLabelDicts:

        valueFrequency = 0
        for numClassification in value.values():
            valueFrequency += numClassification

        valueEntropy = 0
        for numClassification in value.values():
            if numClassification != 0:
                classRatio = (1.0 * numClassification) / valueFrequency
                valueEntropy += classRatio * log2(classRatio)

        entropy += (-1.0 * valueFrequency / totalInstances) * valueEntropy

    return entropy