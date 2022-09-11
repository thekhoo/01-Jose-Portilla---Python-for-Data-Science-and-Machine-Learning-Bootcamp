# 81 - Machine Learning with Python

## Installing `scikit-learn`

`scikit-learn` is the package that will be used for Machine Learning with Python. `scikit-learn` can be installed with `pip install scikit-learn`.

Every algorithm in `scikit-learn` is exposed via an "Estimator". The general form is: `from sklearn.family import Model`.

To import the linear regression model into the Python workspace:

```py
from sklearn.linear_model import LinearRegression
```

In this case, the LinearRegression is the estimator model.

**Estimator Parameters**
All the parameters of an estsimator can be set when it is instantiated, and have suitable default values.

```py
model = LinearRegression(normalize=True)
print(model)

LinearRegression(copy_X=True,fit_intercept=True,normalize=True)
```

## Splitting Data into Train and Test

```py
import numpy as np
from sklearn.model_selection import train_test_split
X, y = np.arange(10).reshape((5,2)), range(5)

# Using train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3)

# Fitting Model on Training Data
model.fit(X_train,y_train)

# Predicting values from model on Testing Data
predictions = model.predict(X_test)

# Evaluate Model...
```