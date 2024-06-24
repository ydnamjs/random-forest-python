# random-forest-python
Python Implementation of Random Forest machine learning algorithm for learning purposes

It comes with a data set (in data directory) for classifying tweets as spam or not spam

## Technologies Used
- Python 3

## Installation and Usage
1. Clone the repository: `git clone https://github.com/username/project.git](https://github.com/ydnamjs/personal-website.git](https://github.com/ydnamjs/random-forest-python.git`
2. Navigate into the repository src directory: `cd random-forest-python/src/`
3. Run the program: `python -m main`

## What is a Decision Tree?
A decision tree is a structure for classifying objects based on features. For example, you might predict if a car has good fuel efficiency based on its weight, the number of cylinders in its engine, how old it is and a number of other things.

The decision tree is a tree structure of splits on these features to try and maximize entropy of a decision. Entropy is a measure of how good that feature is at telling us the output. 

For example, if we were building a decision tree for car efficiency using the data below, our tree would prefer to split on weight rather than num cylinders, because that feature tells us more about the likelihood of having good or bad fuel efficiency

| Weight | Good Fuel Efficiency | Bad Fuel Efficiency |
| --- | --- | ----------- |
| Heavy | 10% | 90% |
| Light | 90% | 10% |

| Num Cylinders | Good Fuel Efficiency | Bad Fuel Efficiency |
| --- | --- | ----------- |
| 4 | 60% | 40% |
| 6 | 40% | 60% |

Decision trees are a tree of splits that you follow like a flow chart to arrive at the most likely value. When we run out of attributes to split on or reach a maximum depth as specified by the user, we pick the most likely value from our subset of data. After we split we isolate the instances from each value of the split. 

In the below example, after we split on weight, we only consider light cars on further splits that happen on the left and heavy cars on further splits that happen on the right. When we reach our limit our decision is based on only cars that have those qualities so for our bottom left decision, we look at all cars that are light and new and base our probability on that.

![image](https://github.com/ydnamjs/random-forest-python/assets/79230564/bcdce79f-64c8-4c36-b8b3-334930951c50)

## What is a Random Forest?

A random forest is a collection of decision trees where each tree is given a random subset of the training data and a random subset of features it can use. Sticking with the car example: Decision Tree A might only be allowed to use the car's age, its weight, number of cylinders, and tire size while Decision Tree B might be allowed to use the car's top speed, its manufacturer, and its tire size. They also might have different cars to use as their training data.

Once we have a random forest, we predict by getting the prediction of every tree and using the most popular one. So if we have 8 trees that think the car has good fuel efficiency and 3 that think the car has bad fuel efficiency, the forest goes with good fuel efficiency.

## Configuration Options

In main.py, there are 5 configurable options for tuning the random forest

NUM_TREES is the number of decision trees in a random forest

TREE_DEPTH is the maximum number of splits decision trees are allowed to make

TREE_FEATURES is the number of features each tree is given to choose from when making splits

TREE_SAMPLE_RATIO is the portion of the random forest's data that each tree is given

FOLD_COUNT is the number of folds used for testing the effectiveness of the random forest

## Performance

With the twitter dataset which has ~600 rows of data and the follow parameters:

`NUM_TREES = 1000`

`TREE_DEPTH = 4`

`TREE_FEATURES = 8`

`TREE_SAMPLE_RATIO = 30/100`

`FOLD_COUNT = 10`

The average performance of the tree was

- Accuracy: 0.7417884278199882

- Precision: 0.75

- Recall: 0.019205465587044536

- F1 Score: 0.12016806722689077

## Limitations

While the decision tree and random forest (should) work for non-boolean classification, the statistics do not as those were just for the assignment

Data parsed with parseData function feature values are limited to 3 options as all features with more than 3 values were binned to prevent splitting 1000 branches on something like number of characters for the twitter data

The algorithm is written in pure python so it is not nearly as fast with large datasets as something that makes use of a proper library like numpy
