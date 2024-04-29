from random import randint
from math import floor
from typing import Dict
from decision_tree.Predict import Predict
from decision_tree._DecisionTree import MakeDecisionTree
from decision_tree._DecisionTree import TreeNode
from parseData import parseData

# CONFIG
NUM_TREES = 25 # number of trees in a random forest
TREE_DEPTH = 3 # maximum depth of a tree
TREE_FEATURES = 7 # number of features a tree is to be given (chosen at random from the total)
TREE_SAMPLE_RATIO = 50/100 # portion of the data the tree is given to be trained (chosen at random from forest training data)
FOLD_COUNT = 5 # number of folds for testing random forest success

# NAME OF LABEL AS IN PARSE DATA DO NOT EDIT
LABEL_NAME = "class"


def MakeRandomForest(numTrees: int, trainingData: list[Dict[str, int]])-> list[TreeNode]:

    trees: list[TreeNode] = []

    featureNames = []
    for key in trainingData[0].keys():
        if key != LABEL_NAME:
            featureNames.append(key)

    for i in range(0, numTrees):
        treeFeatureSet = sampleRandomFeatures(featureNames, TREE_FEATURES)
        filteredFeatures = filterInFeatures(treeFeatureSet, trainingData)
        treeData = sampleRandomRows(filteredFeatures, floor(len(trainingData) * TREE_SAMPLE_RATIO))
        trees.append(MakeDecisionTree(treeData, TREE_DEPTH, LABEL_NAME))

    return trees

def ForestPredict(forest: list[TreeNode], row: Dict[str, int]):

    predictions = {}

    for tree in forest:
        result = Predict(row, tree)

        predictionTotal = predictions.get(result)

        if predictionTotal is None:
            predictions[result] = 1
        else:
            predictions[result] = predictionTotal + 1

    mostFrequentAmount = 0
    mostFrequentClass = None

    for prediction in predictions.keys():
        frequency = predictions.get(prediction)
        if frequency > mostFrequentAmount:
            mostFrequentAmount = frequency
            mostFrequentClass = prediction
    
    if mostFrequentClass is None:
        raise ValueError()

    return mostFrequentClass

def sampleRandomFeatures(featureList: list[str], numFeatures):
    cloneList = featureList.copy()
    samples = []
    for i in range(0, numFeatures):
        randIndex = randint(0, len(cloneList) - 1)
        samples.append(cloneList[randIndex])
        cloneList.pop(randIndex)

    return samples

def filterInFeatures(featuresToKeep: list[str], data: list[Dict[str, int]]):

    filteredData = []
    for oldRow in data:
        newRow = {}
        for feature in featuresToKeep:
            newRow[feature] = oldRow[feature]
        newRow[LABEL_NAME] = oldRow[LABEL_NAME]
        filteredData.append(newRow)

    return filteredData

def sampleRandomRows(data: list[Dict[str, int]], numSamples):

    samples = []
    for i in range(0, numSamples):
        samples.append(data[randint(0, len(data) - 1)])

    return samples

def createDataFolds(data: list[Dict[str, int]], numFolds: int)->list[list[Dict[str, int]]]:

    dataClone = data.copy()

    folds = []
    for i in range(0, numFolds):
        folds.append([])

    foldIndex = 0
    while len(dataClone) != 0:
        randIndex = randint(0, len(dataClone) - 1)
        folds[foldIndex].append(dataClone[randIndex])
        dataClone.pop(randIndex)
        foldIndex = foldIndex + 1
        if foldIndex > numFolds - 1:
            foldIndex = 0

    return folds

def getSplitFolds(folds: list[list[Dict[str, int]]], foldIndex: int):
    testFold = folds[foldIndex]
    trainingFolds = []

    for i in range(0, len(folds)):
        if i != foldIndex:
            trainingFolds.append(folds[i])

    return [testFold, trainingFolds]

def mergeTrainingFolds(folds: list[list[Dict[str, int]]])->list[Dict[str, int]]:

    mergedFolds = []

    for fold in folds:
        for row in fold:
            mergedFolds.append(row)

    return mergedFolds

def averageList(nums: list[float])->float:
    
    if len(nums) == 0:
        return None
    
    total = 0.0
    for num in nums:
        total = total + num
    return total / len(nums)

def main():
    data = parseData()

    folds = createDataFolds(data, FOLD_COUNT)

    results = []

    for i in range(0, len(folds)):

        [testingFold, trainingFolds] = getSplitFolds(folds, i)
        randomForest = MakeRandomForest(NUM_TREES, mergeTrainingFolds(trainingFolds))

        tp = 0; fp = 0; tn = 0; fn = 0

        for row in testingFold:
            prediction = ForestPredict(randomForest, row)
            truth = row.get(LABEL_NAME)

            if truth == 1 and prediction == 1:
                tp = tp + 1
            elif truth == 0 and prediction == 1:
                fp = fp + 1
            elif truth == 0 and prediction == 0:
                tn = tn + 1
            elif truth == 1 and prediction == 0:
                fn = fn + 1

        results.append([tp, fp, tn, fn])

    accs = []
    precs = []
    recalls = []
    f1Scores = []

    for i in range(0, len(results)):
        result = results[i]
        tp = result[0]
        fp = result[1]
        tn = result[2]
        fn = result[3]

        if (tp + tn + fp + fn) != 0:
            acc = (tp + tn) / (tp + tn + fp + fn)
        else:
            acc = None

        if (tp + fp) != 0:
            prec = tp / (tp + fp)
        else:
            prec = None
        
        if (tp + fn) != 0:
            reca = tp / (tp + fn)
        else: 
            reca = None

        if reca is None or prec is None or (prec + reca) == 0:
            f1Score = None
        else:
            f1Score = 2 * ((prec * reca) / (prec + reca))

        print("TEST FOLD IS FOLD #" + str(i + 1) + ":")
        print("Accuracy: " + str(acc))
        print("Precision: " + str(prec))
        print("Recall: " + str(reca))
        print("F1 Score: " + str(f1Score))
        print("")

        if not (acc is None):
            accs.append(acc)
        if not (prec is None):
            precs.append(prec)
        if not (reca is None):
            recalls.append(reca)
        if not (f1Score is None):
            f1Scores.append(f1Score)

    avgAcc = averageList(accs)
    avgPrec = averageList(precs)
    avgReca = averageList(recalls)
    avgF1Score = averageList(f1Scores)

    print("")
    print("AVERAGES")
    print("Accuracy: " + str(avgAcc))
    print("Precision: " + str(avgPrec))
    print("Recall: " + str(avgReca))
    print("F1 Score: " + str(avgF1Score))

main()