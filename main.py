features = [
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

LABELS_PATH = "./data/labeled_tweets.txt"
FEATURE_PATH = "./data/tweet_feature.txt"

LABELS_FILE = open(LABELS_PATH, "r")
FEATURES_FILE = open(FEATURE_PATH, "r")

LABELS_LINES = LABELS_FILE.readlines()
FEATURES_LINES = FEATURES_FILE.readlines()

if(len(LABELS_LINES) != len(FEATURES_LINES)):
    print("BAD DATA: NUMBER OF LINES DONT MATCH")
    exit

labels = []
for line in LABELS_LINES:

    # Class is the last value
    labels.append(line.strip().split("\t")[-1])

rawFeatureSets = []
for line in FEATURES_LINES:
    
    newFeatures = line.strip().split("\t")

    rawFeatures = []
    # First 2 features are identifiers
    for i in range(2, len(newFeatures)):
        rawFeatures.append(int(newFeatures[i]))

    rawFeatureSets.append(rawFeatures)

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

for featureBinSet in featureBinSets:
    print(featureBinSet)