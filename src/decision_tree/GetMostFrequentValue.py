from typing import Dict

def GetMostFrequentLabel(labels: list[int])->int:

    if len(labels) == 0:
        raise ValueError("GET MOST FREQUENT LABEL CALLED WITH EMPTY LIST")

    labelCounts: Dict[int, int] = {}

    for label in labels:

        frequency = labelCounts.get(label)

        if (frequency is None):
            labelCounts[label] = 1
        else:
            labelCounts[label] = labelCounts[label] + 1

    highestFrequency = float("-inf")
    for value in labelCounts.values():
        if value > highestFrequency:
            highestFrequency = value

    for key in labelCounts.keys():
        if labelCounts.get(key) == highestFrequency:
            return key