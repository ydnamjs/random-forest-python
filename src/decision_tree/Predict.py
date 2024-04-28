from typing import Dict
from decision_tree._DecisionTree import TreeNode

def Predict(row: Dict[str, int], node: TreeNode)->int:

    if node.splitAttribute == "none":
        return node.prediction

    rowSplitValue = row.get(node.splitAttribute)

    if rowSplitValue is None:
        raise ValueError("Attempted to predict with attribute not present in row")

    nextNode = node.next.get(rowSplitValue)

    if nextNode is None:
        return node.prediction

    return Predict(row, nextNode)