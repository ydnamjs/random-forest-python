from typing import Dict

def ExtractFeatureValues(data: list[Dict[str, int]], featureName: str)->list[int]:
    values = []
    for row in data:
        value = row.get(featureName)

        if value is None:
            raise ValueError("Attempted to get value of nonexistent feature in getValues feature:" + featureName)

        values.append(value)

    return values