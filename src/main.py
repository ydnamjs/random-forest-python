from decision_tree.Predict import Predict
from decision_tree._DecisionTree import MakeDecisionTree
from parseData import parseData

data = parseData()



root = MakeDecisionTree(data, 8, "class")

result = Predict(data[0], root)
print(result)