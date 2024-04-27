from decision_tree.CalcConditionalEntropy import CalcConditionalEntropy
from parseData import parseData

featuresValuesData = {
    0: {
        0: 1,
        1: 1,
    },
    1: {
        0: 0,
        1: 4,
    },
}

#print(calcConditionalEntropy(featuresValuesData.values()))

data = parseData()

for row in data:
    print(row)