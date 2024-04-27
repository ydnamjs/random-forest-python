from typing import Dict

def MakeValueLabelDict(values: list[int], labels: list[int])->Dict[int, Dict[int, int]]:

    if len(values) != len(labels):
        raise ValueError("Attempted to make value label dict when # values does not match # of labels")
    
    if len(values) == 0:
        raise ValueError("Attempted to make value label dict with no data")

    valueLabelDicts: Dict[int, Dict[int, int]] = {}
    for i in range(0, len(values)):
        value = values[i]
        label = labels[i]

        valueLabelDict = valueLabelDicts.get(value)

        if valueLabelDict is None:
            newLabelDict = {}
            newLabelDict[label] = 1
            valueLabelDicts[value] = newLabelDict
        else:
            labelDict = valueLabelDict.get(label)

            if labelDict is None:
                newLabelDict = {}
                newLabelDict[label] = 1
                valueLabelDict[label] = newLabelDict
            else:
                labelDict[label] = labelDict.get(label) + 1

    return valueLabelDicts