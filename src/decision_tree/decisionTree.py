from dataclasses import dataclass
from typing import Dict

from decision_tree.GetMostFrequentValueTest import getMostFrequentLabel

LABEL_CLASS_NAME = "class"

FEATURE_NAMES = [
    "User Age", 
    "User Description Length", 
    "User Follower Count", 
    "User Friends Count",
    "User Favorites",
    "User Lists",
    "User Statuses Count",
    "Hashtag Count",
    "Mention Count",
    "URL Count",
    "Text Length",
    "Text Digits",
    "Retweeted Favorites Count",
    "Is Truncated",
    "User Is Default",
    "Number Us"
]

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

    if maxDepth == 0:
        return TreeNode(True, "none", getMostFrequentLabel(trainingData))

    bestSplitAttribute = ""
    bestSplitEntropy = float("inf")

    for featureDict in trainingData:
        pass

    print("error not implemented")
    return

def getValueLabelDicts(feature: str, trainingData: list[Dict[str, int]])->Dict[int, Dict[int, int]]:
    
    valueLabelDicts = Dict[int, Dict[int, int]] = {}
    
    for row in trainingData:
        value = row.get(feature)
        label = row.get(LABEL_CLASS_NAME)

        if (label is None or value is None):
            exit()

        valueDict = valueLabelDicts.get(value)
        if (valueDict is None):
            valueLabelDicts[value] = {}
            valueLabelDicts.get(value)[label] = 1
        else:
            labelDict = valueDict.get(label)

            if (labelDict is None):
                labelDict[label] = 1
            else:
                labelDict[label] = labelDict.get(label) + 1
    return valueLabelDicts