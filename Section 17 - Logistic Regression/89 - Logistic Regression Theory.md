# 89 - Logistic Regression Theory

* Logistic Regression as a method of **Classification**
* Some examples of classification problems *(Binary Classification)*:
    * Spam versus "Ham" emails
    * Loan Default (Yes/No)
    * Disease Diagnosis

* Can't use normal linear regression model on binary groups *(Won't be a good fit, data will either be 1 or 0)*
* Transform linear regression curve to a logistic regression curve *(Only goes between 0 and 1)*
* The **Sigmoid Function** takes in a value and outputs it to be between 0 and 1

$$
    \phi (z) = 1 / (1 + e^-z)
$$

* Cutoff at 0.5
    * *Less than 0.5 - Bottom Category*
    * *More than 0.5 - Top Category*