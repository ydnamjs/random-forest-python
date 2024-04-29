# random-forest-python
Python Implementation of Random Forest machine learning algorithm for learning purposes

It comes with a data set (in root/data) for classifying tweets as spam or not spam

# How To Run
in directory src run 
  
```python -m main```

# Rough Description of How It Works

It divides data into folds for cross validation and then creates random forests with the training data. Random forests are a for loop of making decision trees.

Decision trees are formed by recursively creating sub trees. A given subtree splits on the attribute with the lowest conditional entropy and then divides the data among those split values. The divided data is then used to make the tree’s children. The recursion is performed until the tree hits its max depth or until it runs out of features at which point it returns a leaf node that evaluates to the most frequent label.

The random forest will classify a data point by way of popular vote of each of its trees.

# Performance

Performance was measured using 10 fold cross validation with the tweet data set and overall is not too bad for only having ~600 rows of data

Here is the average of the stats for a 10 fold cross validation I ran

Accuracy: 0.762478082992402

Precision: 0.8

Recall: 0.11804793847363507

F1 Score: 0.21903913080383672

# Limitations

while the decision tree and random forest (should) work for nonbinary classification, the statistics do not as those were just for the assignment

data parsed with parseData fucntion feature values are limited to 3 options as all features with more than 3 values were binned to prevent splitting 1000 branches on something like number of characters for the twitter data

the algorithm is written in pure python so it is not nearly as fast with large datasets as something that makes use of a proper library like numpy
