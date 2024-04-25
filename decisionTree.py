import math   
from dataclasses import dataclass
from typing import Dict
from typing import Union

@dataclass
class TreeNode:
    next: Union['TreeNode', int]

def makeDecisionTree(trainingData: list[Dict[str, int]], maxDepth: int):
    """
        @param trainingData: list of a dictionary that maps each feature to its value
            each element is an instance/row of training data
        
        @param maxDepth: the maximum depth of the tree/subtree
    """

    if maxDepth == 0:
        return getMostFrequentLabel(trainingData)


    pass

def getMostFrequentLabel(trainingData: list[Dict[str, int]])->str:

    labelCounts: Dict[str, int] = {}

    for row in trainingData:
        label = row.get("class")

        if label is None:
            exit()

        currValue = labelCounts.get(label)

        if (currValue is None):
            labelCounts[label] = 1
        else:
            labelCounts[label] = labelCounts[label] + 1
    
    highestFrequency = int(float("-inf"))
    for value in labelCounts.values():
        if value > highestFrequency:
            highestFrequency = value
    
    for key in labelCounts.keys():
        if labelCounts.get(key) == highestFrequency:
            return key
    
    return "ERROR"

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
                valueEntropy += classRatio * math.log2(classRatio)

        entropy += (-1.0 * valueFrequency / totalInstances) * valueEntropy

    return entropy