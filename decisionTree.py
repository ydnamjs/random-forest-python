import math   
from dataclasses import dataclass
from typing import Dict

def calcConditionalEntropy(featureValuesData: list[Dict[int, int]])->float:
    """
        @param featureValuesData: Dict of feature value to Dict of label to frequency
            For example we might have a feature: favorite animal where 0 is a dog, 1 is a cat, and 2 is a fish
            And say we are classifying if they are a serial killer or not 0 is no 1 is yes
            And say there are 6 dog lovers that are not serial killers, 3 dog lovers that are serial killers,
            4 cat lovers that are not serial killers, 7 cat lovers that are serial killers,
            5 fish lovers that are not serial killers, and 9 fish lovers that are serial killers
            our featureValueData would then be {0: {0: 6, 1: 3;}; 1: {0: 4, 1: 7}, 2: {0: 5, 1: 9}}

        @returns the entropy of splitting on this feature
    """

    totalInstances = 0
    for value in featureValuesData:
        for classAmt in value.values():
            totalInstances += classAmt

    entropy = 0
    for value in featureValuesData:

        valueFrequency = 0
        for numClassification in value.values():
            valueFrequency += numClassification

        valueEntropy = 0
        for numClassification in value.values():
            if numClassification != 0:
                classRatio = (1.0 * numClassification) / valueFrequency
                valueEntropy += classRatio * math.log2(classRatio)

        entropy += (-1.0 * valueFrequency / totalInstances) * valueEntropy

    return entropy