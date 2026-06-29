# Mathematical Foundations & Linear Algebra (Part 1 & Part 2)

### Scalar

A scalar is simply one single numerical value. Think of it as a variable that stores only one number.

* It has **magnitude only** (no direction).
* Examples: Learning rate, Bias, Loss, Individual Weight.

### Vector

A vector is an **ordered collection of numerical values**.

* It represents multiple related quantities.
* The **order of elements matters**.
* A vector with **n** real numbers belongs to **ℝⁿ**.
* In AI/ML, vectors represent **features, embeddings, probability distributions, hidden states, and model parameters**.

### Matrix

A matrix is a collection of numbers arranged in **rows and columns**.

* Matrix size is written as **Rows × Columns (m × n)**.
* **Rows = Samples (Observations/Records)**
* **Columns = Features**
* Most machine learning datasets are represented as matrices.

### Function

A function maps **input → output**.

* Mathematical notation: **y = f(x)**
* Every Machine Learning model is essentially a mathematical function.
* Input = Features, Output = Prediction.

### Summation (Σ)

The symbol **Σ (Sigma)** means **summation (addition)**.

* **Σᵢ₌₁ⁿ xᵢ** means add all values from **x₁** to **xₙ**.
* Widely used in averages, loss functions, dot products, gradients, and matrix operations.

---

## Part 2

### Vector Space

A vector space is a collection of vectors.
You can:

1. Add vectors.
2. Multiply vectors by scalars.

After these operations, you remain in the same space (Closure Property).

* **ℝ²** is the vector space of all vectors with **2 real-number components**.
* **ℝ³** is the vector space of all vectors with **3 real-number components**.

### Linear Combination

A linear combination is an expression formed by **multiplying vectors by scalars and then adding the results together**.

Formula:

a₁x₁ + a₂x₂ + ... + aₖxₖ

Every prediction in Linear Regression and every neuron in a Neural Network starts with a **weighted linear combination**.

### Span

The span of a set of vectors is the **set of all possible linear combinations** of those vectors.

* Span answers the question: **"What vectors can these vectors generate?"**
* One vector usually spans a **line**.
* Two non-parallel vectors in **ℝ²** span the **entire plane**.

### Basis

A basis is the **smallest set of linearly independent vectors** that can span the entire vector space.

A basis must satisfy two conditions:

1. It spans the entire space.
2. No vector is redundant (linearly independent).

### Dimension

Dimension is the **number of basis vectors** needed to represent a vector space.

Or,

The dimension of a vector space is the **number of vectors in any basis** of that space.

Examples:

* Line → Dimension = **1**
* Plane (ℝ²) → Dimension = **2**
* Space (ℝ³) → Dimension = **3**

In Machine Learning, the **number of features** usually represents the **dimension of the feature space**.

---

## Easy Memory Flow

Scalar
→ One value

Vector
→ Collection of numbers

Matrix
→ Collection of vectors (Rows × Columns)

Function
→ Input → Output

Σ (Sigma)
→ Add all values

Vector Space
→ Collection of valid vectors

Linear Combination
→ Scalar × Vector + Scalar × Vector + ...

Span
→ All possible linear combinations

Basis
→ Minimum linearly independent vectors that span the space

Dimension
→ Number of vectors in the basis

# Part 3: Core Operations

### Dot Product

The **dot product** is obtained by **multiplying corresponding elements of two vectors and adding the results**.

**Formula:**

x · y = Σ xᵢyᵢ

**Geometric Formula:**

x · y = ||x|| ||y|| cosθ

Where:

* **θ** = Angle between vectors.
* **||x||** = Length (Norm) of vector x.

**Interpretation:**

* **Positive** → Similar direction
* **Zero** → Orthogonal (90°)
* **Negative** → Opposite direction

**Key Points:**

* Returns a **Scalar**.
* Measures **directional similarity (alignment)**.

**Applications:**

* Linear & Logistic Regression
* Neural Networks (wᵀx)
* Transformers (Attention)
* Recommendation Systems
* Cosine Similarity

---

# Norms

A **Norm** measures the **length (magnitude)** of a vector.

## L2 Norm (Euclidean Norm)

**Formula:**

||x||₂ = √(Σxᵢ²)

* Measures **straight-line (Euclidean) distance**.
* Shape: **Circle**

```text
      ○
   ○     ○
 ○    •    ○
   ○     ○
      ○
```

**Applications:**

* Gradient Descent
* Ridge (L2) Regularization
* Distance Metrics (KNN)

---

## L1 Norm (Manhattan Norm)

**Formula:**

||x||₁ = Σ|xᵢ|

* Measures **Manhattan (city-block) distance**.
* Shape: **Diamond**

```text
      ♦
    ♦   ♦
  ♦   •   ♦
    ♦   ♦
      ♦
```

**Applications:**

* Lasso (L1) Regularization
* Sparse Models
* Feature Selection

---

### L1 vs L2

| L2 Norm                 | L1 Norm                |
| ----------------------- | ---------------------- |
| Euclidean Distance      | Manhattan Distance     |
| Circle                  | Diamond                |
| Ridge Regularization    | Lasso Regularization   |
| Penalizes large weights | Produces sparse models |

---

# Orthogonality

Two vectors are **orthogonal** if they are **perpendicular (90°)**.

**Condition:**

x · y = 0

**Reason:**

x · y = ||x|| ||y|| cosθ

Since **cos(90°) = 0**, therefore **x · y = 0**.

```text
      ↑
      │
──────┼──────→
     90°
```

**Key Points:**

* Orthogonal vectors are **independent in direction**.
* They contain **non-overlapping information**.

**Applications:**

* PCA
* Orthogonal Weight Initialization
* Feature Engineering
* Word Embeddings

---

## Easy Memory Flow

Dot Product
→ Multiply corresponding elements + Add
→ Measures directional similarity

Norm
→ Length (Magnitude) of a vector

L2 Norm
→ Straight-line distance (Circle)

L1 Norm
→ Manhattan distance (Diamond)

Orthogonality
→ Dot Product = 0
→ 90° (Perpendicular)
→ Independent directions

# Mathematical Foundations & Linear Algebra (Part 4, Part 5 & Part 6)

---

# Part 4: Projections & Least Squares

## Projection

Projection measures **how much one vector lies in the direction of another vector**.

**Formula:**

projᵧ(x) = (x · y / y · y) y

or

projᵧ(x) = (x · y / ||y||²) y

### Key Points

* Projection always requires **two vectors**.
* Returns a **Vector**.
* Keeps only the component along the chosen direction.
* Measures directional contribution.

### Applications

* PCA
* Linear Regression
* Signal Processing
* Dimensionality Reduction

---

## Orthogonal Decomposition

Any vector can be decomposed into:

**x = x̂ + e**

Where:

* **x̂** = Projection
* **e** = Residual (Error)

### Important Property

**x̂ · e = 0**

Projection and residual are always **orthogonal (perpendicular)**.

### Interpretation

Original Vector

=

Projection

*

Perpendicular Residual

### Applications

* Linear Regression
* PCA
* Optimization
* Error Analysis

---

## Least Squares

Least Squares finds the **best approximate solution** when an exact solution does not exist.

Given:

**Ax = b**

### Goal

Minimize:

**||Ax − b||²**

### Normal Equation

**x = (AᵀA)⁻¹Aᵀb**

### Why Square the Error?

* Prevents positive and negative errors from canceling.
* Penalizes larger errors.
* Easier to optimize mathematically.

### Applications

* Linear Regression
* Polynomial Regression
* Curve Fitting
* Computer Vision
* Signal Processing

---

## Easy Memory Flow

Projection

→ Part of a vector along another vector

Orthogonal Decomposition

→ Projection + Residual

Least Squares

→ Minimize Sum of Squared Errors

---

# Part 5: Matrices & Transformations

## Matrix Multiplication

Matrix multiplication combines **multiple linear transformations into one transformation**.

**Formula:**

**C = AB**

### Condition

If

**A (m × n)**

and

**B (n × p)**

then

**AB = (m × p)**

Columns of the first matrix must equal the rows of the second matrix.

### Key Points

* Uses **Row × Column Dot Product**.
* Matrix multiplication is **not commutative**.

**AB ≠ BA**

### Applications

* Neural Networks
* PCA
* Linear Regression
* Computer Graphics

---

## Matrix-Vector Product

A matrix transforms an input vector into a new output vector.

**Formula:**

**Ax**

### Interpretation

* Matrix = Transformation
* Vector = Input
* Output = Transformed Vector

### Key Points

* Returns a **Vector**.
* Each output element is a **Row × Vector Dot Product**.

### Applications

* Neural Networks
* Linear Regression
* PCA
* Computer Graphics

---

## Identity Matrix

Identity Matrix behaves like multiplication by **1**.

**Formula:**

**Ix = x**

### Properties

* Square Matrix
* Main diagonal = 1
* Remaining elements = 0

### Applications

* Matrix Inversion
* Optimization
* Residual Networks (ResNet)

---

## Transpose

Transpose swaps **rows and columns**.

**Formula:**

**(Aᵀ)ᵢⱼ = Aⱼᵢ**

### Key Points

* Rows become Columns.
* Columns become Rows.

### Applications

* Covariance Matrix
* Linear Regression
* Backpropagation
* Matrix Multiplication

---

## Symmetric Matrix

A matrix is symmetric if:

**A = Aᵀ**

### Properties

* Real Eigenvalues
* Orthogonal Eigenvectors

### Applications

* PCA
* Covariance Matrix
* Spectral Methods
* Optimization

---

## Easy Memory Flow

Matrix Multiplication

→ Combine Transformations

Matrix-Vector Product

→ Transform a Vector

Identity Matrix

→ Matrix Version of 1

Transpose

→ Swap Rows & Columns

Symmetric Matrix

→ Equal to Its Transpose

---

# Part 6: Rank & Linear Independence

## Linear Independence

Vectors are **linearly independent** if **no vector can be represented as a linear combination of the others**.

Mathematical Condition:

**a₁x₁ + a₂x₂ + ... + aₙxₙ = 0**

has only the trivial solution:

**a₁ = a₂ = ... = aₙ = 0**

### Interpretation

* No redundancy.
* Every vector contributes **new information**.

If one vector can be created from the others, the vectors are **linearly dependent**.

### Applications

* Feature Selection
* PCA
* Linear Regression

---

## Rank

Rank is the **number of linearly independent rows or columns** in a matrix.

### Interpretation

Rank = Number of unique (non-redundant) rows or columns.

### Full Rank

* No redundancy.
* Every row/column contributes new information.

### Low Rank

* Redundant rows/columns.
* Less unique information.

### Applications

* PCA
* Feature Selection
* Linear Regression
* Detecting Multicollinearity

---

## Easy Memory Flow

Linear Independence

→ No Redundancy

↓

Rank

→ Number of Independent Rows/Columns

↓

Full Rank

→ No Redundancy

↓

Low Rank

→ Redundant Information

---

# Overall Memory Flow (Part 4 → Part 6)

Projection

→ Part of a vector along another vector

↓

Orthogonal Decomposition

→ Projection + Residual

↓

Least Squares

→ Best Fit by Minimizing Squared Error

↓

Matrix Multiplication

→ Combine Transformations

↓

Matrix-Vector Product

→ Transform a Vector

↓

Identity Matrix

→ Matrix Version of 1

↓

Transpose

→ Swap Rows & Columns

↓

Symmetric Matrix

→ Equal to Its Transpose

↓

Linear Independence

→ No Redundancy

↓

Rank

→ Count of Independent Rows/Columns