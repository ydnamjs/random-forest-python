from dataclasses import dataclass
from typing import Dict

from decision_tree.GetMostFrequentValueTest import getMostFrequentLabel
from decision_tree.CalcConditionalEntropy import calcConditionalEntropy

LABEL_NAME = "class"

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

    if maxDepth == 0 or len(trainingData) == 0:
        return TreeNode(True, "none", getMostFrequentLabel(getValues(trainingData, LABEL_NAME)))

    bestSplitAttribute = ""
    bestSplitEntropy = float("inf")

    for featureDict in trainingData:
        featureEntropy = calcConditionalEntropy()

    print("error not implemented")
    return

def getValues(data: list[Dict[str, int]], featureName: str)->list[int]:
    values = []
    for row in data:
        value = row.get(featureName)

        if value is None:
            raise ValueError("Attempted to get value of nonexistent feature in getValues feature:" + featureName)

        values.append(value)

    return values