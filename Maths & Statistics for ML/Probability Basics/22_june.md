# Probability Basics & Advanced Probability Notes

These notes cover the probability concepts discussed, including the different types of probability, advanced probability concepts, Bayes' Theorem, and probability distributions. The notes are concise, beginner-friendly, and suitable for AI/ML preparation.

---

# 1. Types of Probability

Probability can be classified into three main types depending on how it is calculated.

---

## 1.1 Classical Probability (Theoretical Probability)

### Definition

Classical probability is used when all possible outcomes are **equally likely**.

### Formula

```text
P(E) = Favorable Outcomes / Total Outcomes
```

### Example

Rolling a fair six-sided die:

```text
P(Getting 3) = 1/6
```

Drawing an Ace from a deck of 52 cards:

```text
P(Ace) = 4/52 = 1/13
```

### Key Points

- Outcomes are equally likely.
- No experiment is required.
- Based purely on mathematics.

---

## 1.2 Relative Frequency (Experimental) Probability

### Definition

Probability calculated from actual experiments or observations.

### Formula

```text
P(E) = Number of times event occurred / Total number of trials
```

### Example

A coin is tossed 20 times.

Heads appears 15 times.

```text
P(Heads) = 15/20 = 0.75
```

### Key Points

- Based on experimental data.
- More trials generally produce more accurate estimates.
- Also called Experimental Probability.

---

## 1.3 Subjective Probability

### Definition

Probability based on personal experience, judgment, or belief.

### Example

- Predicting your favorite cricket team will win.
- Predicting it will rain today based on weather experience.

### Key Points

- No mathematical calculation.
- Based on human judgment.
- Used when exact probabilities are unavailable.

---

# Quick Summary

| Type | Based On | Example |
|------|----------|---------|
| Classical | Mathematics | Rolling a Dice |
| Relative Frequency | Experiments | Coin Toss |
| Subjective | Personal Judgment | Team Winning Prediction |

---

# 2. Advanced Probability

---

## 2.1 Marginal Probability

### Definition

Probability of a **single event**, ignoring all other events.

### Notation

```text
P(A)
```

### Example

Suppose a class has 100 students.

50 are boys.

```text
P(Boy) = 50/100 = 0.5
```

### Key Points

- Considers only one event.
- Uses row totals or column totals.

---

## 2.2 Joint Probability

### Definition

Probability that **two events occur together**.

Think of **AND**.

### Notation

```text
P(A ∩ B)
```

### Example

30 students are Boys and Like Cricket.

```text
P(Boy AND Cricket)

= 30/100

= 0.30
```

### Key Points

- Represents intersection.
- Means both events happen together.

---

## 2.3 Conditional Probability

### Definition

Probability of one event given that another event has already occurred.

### Notation

```text
P(A | B)
```

Read as:

```text
Probability of A given B
```

### Formula

```text
P(A | B) = P(A ∩ B) / P(B)
```

### Example

Among 50 boys,

30 like cricket.

```text
P(Cricket | Boy)

= 30/50

= 0.60
```

### Key Points

- "Given" means one condition is already known.
- Widely used in Machine Learning.

---

# Easy Way to Remember

| Concept | Meaning |
|----------|---------|
| Marginal | Single Event |
| Joint | A AND B |
| Conditional | A GIVEN B |

---

# 3. Bayes' Theorem

## Definition

Bayes' Theorem updates the probability of an event after observing new evidence.

It helps answer questions like:

> "Now that I know this information, how should I update my probability?"

---

## Formula

```text
P(A | B) = [P(B | A) × P(A)] / P(B)
```

Where

- P(A) = Prior Probability
- P(B|A) = Likelihood
- P(B) = Evidence
- P(A|B) = Posterior Probability

---

## Picnic Example

### Given

```text
P(Rain) = 0.15

P(Cloudy) = 0.25

P(Cloudy | Rain) = 0.80
```

Find

```text
P(Rain | Cloudy)
```

Using Bayes' Theorem

```text
P(Rain | Cloudy)

= (0.80 × 0.15) / 0.25

= 0.48
```

### Answer

```text
48%
```

### Interpretation

Initially,

```text
Chance of Rain = 15%
```

After seeing clouds,

```text
Chance of Rain = 48%
```

Clouds act as **new evidence**, increasing the probability of rain.

---

# 4. Probability Distribution

## Definition

A Probability Distribution lists every possible value of a random variable along with the probability of each value occurring.

---

## Example

Rolling a fair die.

| Outcome | Probability |
|----------|-------------|
|1|1/6|
|2|1/6|
|3|1/6|
|4|1/6|
|5|1/6|
|6|1/6|

The total probability is always

```text
1
```

---

# Types of Probability Distribution

```text
Probability Distribution
│
├── Discrete Random Variable
│      └── PMF
│
└── Continuous Random Variable
       └── PDF

Both use

      ↓

CDF
```

---

# 5. Probability Mass Function (PMF)

## Definition

Used for **Discrete Random Variables**.

PMF gives the probability of an **exact value**.

### Examples

- Dice
- Number of Students
- Number of Cars
- Number of Emails

### Example

```text
P(X = 3) = 1/6
```

### Key Points

- Used only for discrete variables.
- Exact probability is possible.

---

# 6. Probability Density Function (PDF)

## Definition

Used for **Continuous Random Variables**.

Examples

- Height
- Weight
- Temperature
- Time

### Important Note

For continuous variables,

```text
P(X = exact value) = 0
```

Instead,

we calculate probability over an interval.

Example

```text
170 cm ≤ Height ≤ 175 cm
```

The probability is the **area under the curve**.

---

# 7. Cumulative Distribution Function (CDF)

## Definition

CDF gives the cumulative probability.

### Formula

```text
P(X ≤ x)
```

### Example

For a dice,

```text
P(X ≤ 3)

= P(1)+P(2)+P(3)

= 1/6 + 1/6 + 1/6

= 3/6

= 0.5
```

### Key Points

- Used for both discrete and continuous variables.
- Adds probabilities from left to right.

---

# 8. Discrete vs Continuous

| Concept | Discrete | Continuous |
|----------|----------|------------|
| Values | Countable | Infinite |
| Example | Dice | Height |
| Function | PMF | PDF |
| Exact Probability | Possible | Always 0 |
| Interval Probability | Sum of PMF | Area Under PDF |
| Cumulative Probability | CDF | CDF |

---

# 9. Python Example (Binomial PMF)

```python
from scipy.stats import binom

n = 100
p = 0.02
x = 3

prob = binom.pmf(x, n, p)

print(prob)
```

### Explanation

```text
n = Number of trials

100
```

```text
p = Probability of success

2%
```

```text
x = Exactly 3 successes
```

```text
binom.pmf(x, n, p)
```

returns

```text
Probability of getting exactly 3 successes
```

### Output

```text
0.18227594104651612
```

Meaning

```text
18.23% chance of exactly 3 successes.
```

---

# 10. Interview Notes

### Marginal Probability

- Single event.
- Ignore other events.

### Joint Probability

- Means AND.
- Uses Intersection (∩).

### Conditional Probability

- Means GIVEN.
- Formula

```text
P(A | B) = P(A ∩ B) / P(B)
```

### Bayes' Theorem

Updates probability after observing new evidence.

### PMF

- Discrete Variables
- Exact Probability

### PDF

- Continuous Variables
- Interval Probability
- Area Under Curve

### CDF

- Cumulative Probability
- Works for both PMF and PDF

---

# Quick Revision

```text
Classical Probability
        ↓
Equal Chances

Relative Frequency
        ↓
Experiments

Subjective
        ↓
Personal Judgment

Marginal
        ↓
Single Event

Joint
        ↓
AND

Conditional
        ↓
GIVEN

Bayes
        ↓
Update Probability After Evidence

PMF
        ↓
Discrete

PDF
        ↓
Continuous

CDF
        ↓
Cumulative Probability
```

---

# Key Takeaways

- Probability measures the likelihood of an event.
- Classical probability assumes equally likely outcomes.
- Relative frequency probability comes from experiments.
- Subjective probability depends on personal belief.
- Marginal probability considers one event.
- Joint probability represents two events occurring together.
- Conditional probability calculates probability given another event.
- Bayes' Theorem updates probabilities using new evidence.
- PMF is used for discrete random variables.
- PDF is used for continuous random variables.
- CDF provides cumulative probabilities.
- The total probability in any probability distribution is always **1**.