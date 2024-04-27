from dataclasses import dataclass
from typing import Dict

from decision_tree.GetMostFrequentValueTest import GetMostFrequentLabel
from decision_tree.CalcConditionalEntropy import CalcConditionalEntropy
from decision_tree.MakeValueLabelDict import MakeValueLabelDict

LABEL_NAME = "class"

@dataclass
class TreeNode:
    isLeaf: bool
    splitAttribute: str
    next: Dict[int, "TreeNode"] | int

def makeDecisionTree(trainingData: list[Dict[str, int]], maxDepth: int)->TreeNode:
    """
        @param trainingData: list of a dictionary that maps each feature to its value
            each element is an instance/row of training data
        
        @param maxDepth: the maximum depth of the tree/subtree
    """

    if maxDepth == 0 or len(trainingData) == 0:
        return TreeNode(True, "none", GetMostFrequentLabel(GetValues(trainingData, LABEL_NAME)))

    firstRow = trainingData[0]
    featureNames = firstRow.keys()
    labels = GetValues(trainingData, LABEL_NAME)

    bestSplitAttribute = ""
    bestSplitEntropy = float("inf")

    for featureName in featureNames:
        featureValues = GetValues(trainingData, featureName)
        valueLabelDicts = MakeValueLabelDict(featureValues, labels)
        featureEntropy = CalcConditionalEntropy(valueLabelDicts.values())

        if featureEntropy < bestSplitEntropy:
            bestSplitEntropy = featureEntropy
            bestSplitAttribute = featureName



    return TreeNode(False, bestSplitAttribute, )

def GetValues(data: list[Dict[str, int]], featureName: str)->list[int]:
    values = []
    for row in data:
        value = row.get(featureName)

        if value is None:
            raise ValueError("Attempted to get value of nonexistent feature in getValues feature:" + featureName)

        values.append(value)

    return values