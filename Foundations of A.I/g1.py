import numpy as np

# --------------------------------------------------
# DATASET
# Each row: [feature1, feature2, ..., feature5, class]
# Last column = class label (0 or 1)
# --------------------------------------------------
data = np.array([
    [0,0,1,1,1,0],[1,0,1,1,0,0],[1,1,0,0,1,0],
    [1,1,0,0,0,0],[0,1,0,0,1,0],[0,0,0,1,0,0],
    [1,0,0,1,1,1],[1,1,0,0,1,1],[1,1,1,1,0,1],
    [1,1,0,1,0,1],[1,1,0,1,1,1],[1,0,1,1,0,1],
    [1,0,1,0,0,1]
])

# --------------------------------------------------
# SPLIT DATA
# X = features, y = labels
# --------------------------------------------------
X, y = data[:, :-1], data[:, -1]


# --------------------------------------------------
# PRIOR PROBABILITIES P(y)
# Probability of each class (0 or 1)
# --------------------------------------------------
priors = {c: np.mean(y == c) for c in [0,1]}


# --------------------------------------------------
# LIKELIHOODS P(x_i | y)
# Probability of feature value given class
# Stored as: (class, feature_index, value)
# --------------------------------------------------
likelihoods = {
    (c, i, v): np.mean(X[y==c][:, i] == v)
    for c in [0,1]                 # class
    for i in range(X.shape[1])     # feature index
    for v in [0,1]                # feature value
}


# --------------------------------------------------
# POSTERIOR P(y | x)
# Using Naive Bayes formula:
# P(y|x) ∝ P(y) * Π P(x_i | y)
# --------------------------------------------------
def posterior(x):
    post = {
        c: priors[c] * np.prod([
            likelihoods[(c, i, v)] for i, v in enumerate(x)
        ])
        for c in [0,1]
    }

    # Normalize probabilities
    s = sum(post.values())
    return {c: post[c]/s for c in post}


# --------------------------------------------------
# ODDS RATIO
# Odds = P(class=1) / P(class=0)
# If > 1 → class = 1 else class = 0
# --------------------------------------------------
def odds(x):
    p = posterior(x)
    o = p[1] / p[0]
    return o, int(o > 1)


# --------------------------------------------------
# LIKELIHOOD RATIO
# Ratio of likelihoods:
# Π [P(x_i|1) / P(x_i|0)]
# Then multiply by prior ratio
# --------------------------------------------------
def likelihood_ratio(x):
    lr = np.prod([
        likelihoods[(1, i, v)] / likelihoods[(0, i, v)]
        for i, v in enumerate(x)
    ])

    # Decision using likelihood ratio + prior ratio
    return lr, int(lr * (priors[1]/priors[0]) > 1)


# --------------------------------------------------
# TEST SAMPLE
# --------------------------------------------------
x = [1,0,1,1,1]

print("Posterior:", posterior(x))
print("Odds:", odds(x))