import math   

def calcConditionalEntropy(featureValueCounts: list[int], labels: list[list[int]])->float:
    '''
    @param featureValueCount: the frequency of each featureValue ex: (3 dog, 5 cat, 1 fish for feature: favorite animal)

    @param labels: the number of each class that each feature value has 
        ex(1 dog lover is a serial killers 2 are not, 2 cat lovers are serial killers, 3 are not, 0 fish lovers are serial killers, 1 fish lover is not)

    @returns entropy: the entropy of splitting on this feature 
    '''

    numInstances = 0
    for count in featureValueCounts:
        numInstances += count


    entropy = 0
    for i in range(0, len(featureValueCounts)):
        
        featureInstances = featureValueCounts[i]

        entropyBuilder = 0
        for j in range(0, len(labels[i])):

            numClassed = labels[i][j]
            if(numClassed != 0):
                portionOfFeatureCount = ((1.0 * numClassed) / featureInstances)
                entropyBuilder += portionOfFeatureCount * math.log2(portionOfFeatureCount)

        entropy += ((-1.0 * featureInstances) / numInstances) * entropyBuilder

    return entropy