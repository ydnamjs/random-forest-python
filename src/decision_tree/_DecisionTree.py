from dataclasses import dataclass
from typing import Dict

from decision_tree.ExtractFeatureValues import ExtractFeatureValues
from decision_tree.GetMostFrequentValue import GetMostFrequentValue
from decision_tree.CalcConditionalEntropy import CalcConditionalEntropy
from decision_tree.MakeValueLabelDict import MakeValueLabelDict
from decision_tree.SplitDataOn import SplitDataOn

@dataclass
class TreeNode:
    """
    @attribute splitAttribute: the feature being split on at this node in the tree

    @attribute children: dictionary of feature value to subtree node

    @attribute prediction: most frequent class value at this node (used for result on leaf nodes and feature values for which no data was available for)
    """
    splitAttribute: str
    next: Dict[int, "TreeNode"]
    prediction: int

def MakeDecisionTree(trainingData: list[Dict[str, int]], maxDepth: int, labelName: str)->TreeNode:
    """
        @param trainingData: list of a dictionary that maps each feature to its value
            each element is an instance/row of training data

        @param maxDepth: the maximum depth of the tree/subtree

        @param labelName: the name of the attribute in the data that is being classified

        @returns a TreeNode used for classification
    """

    if maxDepth == 1 or len(trainingData) == 0:
        return TreeNode("none", {}, GetMostFrequentValue(ExtractFeatureValues(trainingData, labelName)))

    featureNames = []
    for key in trainingData[0].keys():
        if key != labelName:
            featureNames.append(key)

    labels = ExtractFeatureValues(trainingData, labelName)

    bestSplitAttribute = ""
    bestSplitEntropy = float("inf")

    for featureName in featureNames:
        featureValues = ExtractFeatureValues(trainingData, featureName)
        valueLabelDicts = MakeValueLabelDict(featureValues, labels)
        featureEntropy = CalcConditionalEntropy(valueLabelDicts.values())

        if featureEntropy < bestSplitEntropy:
            bestSplitEntropy = featureEntropy
            bestSplitAttribute = featureName

    if bestSplitAttribute == "":
        return TreeNode("none", {}, GetMostFrequentValue(ExtractFeatureValues(trainingData, labelName)))

    children = {}
    partitionedData = SplitDataOn(bestSplitAttribute, trainingData)
    for key in partitionedData.keys():
        children[key] = MakeDecisionTree(partitionedData[key], maxDepth-1, labelName)

    return TreeNode(bestSplitAttribute, children, GetMostFrequentValue(ExtractFeatureValues(trainingData, labelName)))