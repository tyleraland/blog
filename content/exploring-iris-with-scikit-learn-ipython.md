title: Exploring the Iris dataset with scikit-learn and ipython
tags: data, python, machine-learning
date: 2013-07-02

Today I'll share some of the goodies I've found while exploring scikit-learn's tutorial and practice embedding code snippets in posts.  I'll try to avoid just rehashing the tutorial. To get started, scikit-learn (and numpy, which it depends on) should be installed.  I also assume we're using ipython, since it makes exploring objects more fun.  Any '?' or '%' prefixes to the following code snippets are functions of IPython.

```
from sklearn.datasets import load_iris
iris = load_iris()
```
The iris dataset is commonly used among the Machine-Learning/Data-Mining communities. Enough is known about the properties of the data that practitioners are confident using it as a test case for new algorithms and the like. I like that it comes built in! To start, let's pretend we don't know anything about the iris data.

```
iris?              # Not helpful--whhat attributes are available?
iris.         # .DESCR, .data, .target, feature_names ...
print(iris.DESCR)  # Data summary, features and classes...
iris.data?         # Ah, a numpy ndarray
iris.data.shape    # (data_points, features) == (150, 4)
iris.target        # 1-D array of 0's, 1's, and 2's
iris.target.size   # There are 150; these must be the classes
iris.feature_names # Here is the enumerated type to the 0/1/2's
```
numpy's arrays are really nice for indexing and slicing.

```
row, col = 5, 10
iris.data[row]     # Row 5
iris.data[:,col]   # Column 10
iris.data[5,10]    # Element at 5,10
iris.data[[1,2,3]] # Return array of rows 1, 2, and 3
iris.data.argmax() # Largest element in flattened array
iris.data.flatten()[iris.data.argmax()] # 7.9
```
That was just exploring the data with IPython. If we wanted to completely skip that step, we can jump right in and start learning some rules.

```
X,y = iris.data, iris.target      # Training set and classes
from sklearn.svm import LinearSVC # Support Vector Classifer
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# Instantiate each learner
l1 = LinearSVC()
l2 = LogisticRegression()
l3 = KNeighborsClassifier 
new_data =  [[ 5.0, 3.6, 1.3, 0.25]] # Predict its class 

for learner in [l1,l2,l3]:
  learner.fit(X,y)
  print(learner.predict(new_data)) # Each says class-0
```
I like the standard interface to train and use each classifier. In addition, the LogisticRegression learner also assigns a probability to each possible class.

```
l2.predict_proba(new_data) # A list of three floats
                           # [.90, ,09, .00]
l2.predict_proba(new_data).sum() # ~ 1.0
```
Each learner also comes with a "score" method for measuring accuracy relative to provided test and class data. It's straightforward to randomize the data, split it into a 'training' and 'test' set, and compare the learners.

```
import numpy as np                   # We want to use its arrays
from numpy.random import RandomState # Random functions
RandomState.seed(42)
order = np.arange(0,150)             # Flat array, 0..149

# Shuffle the data, determine the training/testing split
RandomState.shuffle(order)           # Randomize order in situ
X = iris.data[order]
y = iris.target[order]
split = 150 * 2 / 3                  # 2/3 training, 1/3 testing

X_train, X_test = X[:split], X[split:]
y_train, y_test = y[:split], y[split:]

# Now train and test
for learner in l1,l2,l3:
  learner.fit(X_train, y_train)
  print(larner.score(X_test,y_test))
```
The resulting scores are .92, .88, and .94 respectively. It appears Nearest Neighbors is the champ today.
