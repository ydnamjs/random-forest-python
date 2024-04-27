from typing import Dict

def SplitDataOn(splitAttribute: str, trainingData: list[Dict[str, int]])->Dict[int, list[Dict[str, int]]]:

    branchesData: Dict[int, list[Dict[str, int]]] = {}

    for row in trainingData:

        splitValue = row.get(splitAttribute)

        if splitValue is None:
            raise ValueError("Unable to find split value in split data on function")

        rowClone = {}
        for key in row:
            rowClone[key] = row[key]
        rowClone.pop(splitAttribute)

        branchData = branchesData.get(splitValue)

        if branchData is None:
            newBranchData = []
            newBranchData.append(rowClone)
            branchesData[splitValue] = newBranchData
        else:
            branchData.append(rowClone)
    
    return branchesData