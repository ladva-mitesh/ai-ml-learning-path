# Statistical Estimation — Quick Notes

## Why Estimation?

### Definition

Statistical Estimation is the process of using **sample (observed) data** to estimate **unknown population parameters**.

> We don't know the true value, so we make the best possible estimate using available data.

### Why do we need Estimation?

* Population is usually too large to observe completely.
* Collecting data from everyone is expensive and time-consuming.
* We use a sample to estimate unknown values.

### Population vs Sample

* **Population:** Entire dataset or data-generating process.
* **Sample:** A subset of the population used for estimation.

### Mathematical Idea

* **Observed Data:** $X$
* **Unknown Parameter:** $\theta$

Goal:

$$
X \longrightarrow \text{Estimate } \theta
$$

### AI/ML Applications

* Linear Regression → Estimate coefficients
* Neural Networks → Estimate weights
* Recommendation Systems → Estimate user preferences
* Bayesian Models → Estimate probability distributions

---

# Part 1 — Point Estimation

## Point Estimate

A **Point Estimate** is a **single numerical value** used to estimate an unknown population parameter.

### Example

Sample marks:

70, 80, 75, 90, 85

Estimated average:

**80**

---

## Why "Point" Estimation?

It gives **one exact value**, not a range.

Example:

* ✅ Average = **170 cm**
* ❌ Average = **168–172 cm** (Interval Estimate)

---

## Mathematical Notation

Population Mean:

$$
\mu
$$

Estimated Mean:

$$
\hat{\mu}
$$

The **hat (^)** denotes an estimated value.

---

## Estimator vs Estimate

### Estimator

A **formula or method** used to calculate an estimate.

Example:

$$
\hat{\mu}=\frac{\sum x_i}{n}
$$

### Estimate

The **actual numerical value** obtained after applying the estimator.

Example:

Sample Mean = **80**

---

## Observed Data

Observed data is the **sample data collected from the real world**.

Example:

Sample:

```
[2, 4, 6]
```

Estimate:

$$
\hat{\mu}=4
$$

---

## Examples of Point Estimation

| Population Parameter | Point Estimator |
| -------------------- | --------------- |
| Mean ($\mu$) | Sample Mean |
| Variance ($\sigma^2$) | Sample Variance |
| Probability ($p$) | Sample Proportion |

---

## Desirable Properties of an Estimator

A good estimator should be:

* Unbiased
* Low Variance
* Consistent
* Efficient

### Unbiased

Expected value equals the true parameter.

$$
E[\hat{\theta}] = \theta
$$

### Variance

Measures how much estimates change across different samples.

Lower variance = More stable estimator.

### Consistency

As sample size increases, the estimate gets closer to the true value.

### Efficiency

Among unbiased estimators, the one with the **lowest variance** is the most efficient.

---

# Part 2 — Bias & Variance

## Bias

Bias is the difference between the estimator's average prediction and the true value.

* High Bias → Predictions are consistently wrong.

---

## Variance

Variance measures how much predictions change when different samples are used.

* High Variance → Predictions fluctuate significantly.

---

## Bias vs Variance

| Bias                          | Variance                             |
| ----------------------------- | ------------------------------------ |
| Measures Accuracy             | Measures Consistency                 |
| High Bias → Wrong predictions | High Variance → Unstable predictions |

---

## Four Cases

### 1. Low Bias + Low Variance ✅

* Accurate
* Consistent
* Best case

### 2. High Bias + Low Variance

* Consistent
* Incorrect predictions

### 3. Low Bias + High Variance

* Accurate on average
* Unstable predictions

### 4. High Bias + High Variance

* Inaccurate
* Inconsistent
* Worst case

---

## Bias–Variance Tradeoff

* Simple model → High Bias, Low Variance
* Complex model → Low Bias, High Variance

Goal:

Find the balance between Bias and Variance.

---

## ML Connection

### Underfitting

* High Bias
* Low Variance

### Overfitting

* Low Bias
* High Variance

---

# Part 3 — Maximum Likelihood Estimation (MLE)

## Definition

**Maximum Likelihood Estimation (MLE)** estimates unknown parameters by choosing values that make the **observed data most likely**.

---

## Intuition

> Find the parameter value that best explains the data.

---

## Coin Toss Example

Observed:

```
H H T H H H T H H H
```

Heads = 8

Estimated probability:

$$
\hat{p}=0.8
$$

because it makes the observed data most likely.

---

## Likelihood

Likelihood measures **how likely the observed data is for a given parameter value**.

Likelihood Function:

$$
L(\theta)=P(X \mid \theta)
$$

where:

* $X$ = Observed data
* $\theta$ = Unknown parameter

MLE chooses the value of $\theta$ that maximizes $L(\theta)$.

---

## Steps in MLE

1. Collect sample data.
2. Write the likelihood function.
3. Maximize the likelihood.
4. Obtain the Maximum Likelihood Estimate (MLE).

---

## AI/ML Applications

MLE is widely used in:

* Linear Regression
* Logistic Regression
* Naive Bayes
* Gaussian Models
* Hidden Markov Models
* Deep Learning

---

# Quick Revision

* **Statistical Estimation:** Estimate unknown parameters using sample data.
* **Point Estimate:** A single best numerical estimate.
* **Estimator:** Formula or method.
* **Estimate:** Numerical result.
* **Observed Data:** Sample collected from the real world.
* **Unbiased:** Correct on average.
* **Variance:** Stability of estimates.
* **Consistency:** Improves with more data.
* **Efficiency:** Lowest variance among unbiased estimators.
* **Bias:** Systematic error.
* **Variance:** Sensitivity to different samples.
* **Underfitting:** High Bias.
* **Overfitting:** High Variance.
* **MLE:** Finds parameter values that make the observed data most likely.
