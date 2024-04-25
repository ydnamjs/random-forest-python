import math   
from dataclasses import dataclass

@dataclass
class FeatureValueData:
    """Data about one of a feature's possible values used for calculating entropy"""
    
    # The value of the feature this class represents ex: value would be dog or cat for feature favorite animal
    # Values are expected to be enumerated so dog would be 0 and cat would be 1 and fish would be 2
    value: int

    # The number of times the value appears in the dataset
    frequency: int

    # A dictionary of label: int (enumerated) to number of times it appears with this value of the feature
    # EX: if 3 dog likers are not serial killers and 6 are, notSerialKiller (0) would map to 3 and isSerialKiller (1) would map to 6
    classifications: dict

def calcConditionalEntropy(featureValuesData: list[FeatureValueData])->float:

    totalInstances = 0
    for value in featureValuesData:
        totalInstances += value.frequency

    entropy = 0
    for value in featureValuesData:

        # Get the entropy for the value of this class
        valueEntropy = 0
        for numClassification in value.classifications.values():
            if numClassification != 0:
                classRatio = (1.0 * numClassification) / value.frequency
                valueEntropy += classRatio * math.log2(classRatio)

        # Add this values weighted entropy to the total
        entropy += (-1.0 * value.frequency / totalInstances) * valueEntropy

    return entropy