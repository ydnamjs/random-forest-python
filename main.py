from decisionTree import calcConditionalEntropy

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

print(calcConditionalEntropy(featuresValuesData.values()))