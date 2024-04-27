from typing import Dict

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

LABELS_PATH = "../data/labeled_tweets.txt"
FEATURE_PATH = "../data/tweet_feature.txt"

def getLabels(labelsLines: list[str])->list[int]:
    labels = []
    for line in labelsLines:

        # Class is the last value
        labels.append(int(line.strip().split("\t")[-1]))
    return labels

def getRawFeatureSets(featuresLines: list[str])->list[list[int]]:
    rawFeatureSets = []
    for line in featuresLines:
        
        newFeatures = line.strip().split("\t")

        rawFeatures = []
        # First 2 features are identifiers
        for i in range(2, len(newFeatures)):
            rawFeatures.append(int(newFeatures[i]))

        rawFeatureSets.append(rawFeatures)
    return rawFeatureSets

def calcFeatureBins(rawFeatureSets)->list[list[int]]:
    maxValues = []
    minValues = []

    for _feature in rawFeatureSets[0]:
        maxValues.append(float("-inf"))
        minValues.append(float("inf"))

    for i in range(0, len(rawFeatureSets)):
        for j in range(0, len(rawFeatureSets[i])):
            if rawFeatureSets[i][j] > maxValues[j]:
                maxValues[j] = rawFeatureSets[i][j]
            if rawFeatureSets[i][j] < minValues[j]:
                minValues[j] = rawFeatureSets[i][j]

    featureBinSets = []
    for i in range(len(maxValues)):

        featureBinSet = []

        if maxValues[i] - minValues[i] < 3:
            for i in range(minValues[i], maxValues[i] + 1):
                featureBinSet.append([i, i])
        else:
            binWidth = (maxValues[i] - minValues[i]) // 3
            featureBinSet.append([float("-inf"), minValues[i] + binWidth])
            featureBinSet.append([minValues[i] + binWidth + 1, minValues[i] + binWidth * 2])
            featureBinSet.append([(minValues[i] + binWidth * 2) + 1, float("inf")])
        featureBinSets.append(featureBinSet)
    
    return featureBinSets

def binFeatures(rawFeatureSets: list[list[int]], featureBinSets: list[list[int]])->list[list[int]]:
    binnedFeatureSets = []
    for i in range(0, len(rawFeatureSets)):
        binnedFeatures = []
        
        for j in range(0, len(rawFeatureSets[i])):

            for k in range(0, len(featureBinSets[j])):
                
                if(rawFeatureSets[i][j] >= featureBinSets[j][k][0] and rawFeatureSets[i][j] <= featureBinSets[j][k][1]):
                    binnedFeatures.append(k)
                    break

        binnedFeatureSets.append(binnedFeatures)
    
    return binnedFeatureSets

def convertDataToDicts(data: list[list[int]], labels: list[int])->list[Dict[str, int]]:
    dataDicts: list[Dict[str, int]] = []
    for i in range(0, len(data)):
        rowDict = {}
        for j in range(0, len(data[0])):
            featureName = FEATURE_NAMES[j]
            rowDict[featureName] = data[i][j]
        rowDict[LABEL_CLASS_NAME] = labels[i]
        dataDicts.append(rowDict)
    
    return dataDicts


def parseData()->list[Dict[str, int]]:

    labelsFile = open(LABELS_PATH, "r")
    featuresFile = open(FEATURE_PATH, "r")

    labelsLines = labelsFile.readlines()
    featuresLines = featuresFile.readlines()

    if(len(labelsLines) != len(featuresLines)):
        print("BAD DATA: NUMBER OF LINES DONT MATCH")
        exit

    labels = getLabels(labelsLines)

    rawFeatureSets = getRawFeatureSets(featuresLines)

    featureBinSets = calcFeatureBins(rawFeatureSets)

    return convertDataToDicts(binFeatures(rawFeatureSets, featureBinSets), labels)
