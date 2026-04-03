import numpy as np # type: ignore

# 1. Read data (Simulated from the provided table)
data = [
    [0, 0, 1, 1, 1, 0], [1, 0, 1, 1, 0, 0], [1, 1, 0, 0, 1, 0],
    [1, 1, 0, 0, 0, 0], [0, 1, 0, 0, 1, 0], [0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 1], [1, 1, 0, 0, 1, 1], [1, 1, 1, 1, 0, 1],
    [1, 1, 0, 1, 0, 1], [1, 1, 0, 1, 1, 1], [1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 1]
]

def get_model(dataset):
    dataset = np.array(dataset)
    X = dataset[:, :-1]
    y = dataset[:, -1]
    
    # 2. Prior Probabilities
    classes, counts = np.unique(y, return_counts=True)
    priors = {c: count / len(y) for c, count in zip(classes, counts)}
    
    # 3. Likelihoods P(xi | y)
    likelihoods = {}
    for c in classes:
        subset = X[y == c]
        for col in range(X.shape[1]):
            # P(xi=1 | y=c)
            prob_1 = np.sum(subset[:, col]) / len(subset)
            likelihoods[(c, col, 1)] = prob_1
            likelihoods[(c, col, 0)] = 1 - prob_1
            
    return priors, likelihoods

priors, likelihoods = get_model(data)

# 4. Posterior Calculation
def get_posterior(x_vec, priors, likelihoods):
    posteriors = {}
    for c in priors:
        prob = priors[c]
        for i, val in enumerate(x_vec):
            prob *= likelihoods.get((c, i, val), 0.001) # Small epsilon for 0
        posteriors[c] = prob
        
    # Normalize
    total = sum(posteriors.values())
    return {c: p / total for c, p in posteriors.items()}

# 5. Odds and Likelihood Ratio
def posterior_odds(x_vec):
    post = get_posterior(x_vec, priors, likelihoods)
    odds = post[1] / post[0]
    label = 1 if odds > 1 else 0
    return odds, label

def likelihood_ratio(x_vec):
    lr = 1.0
    for i, val in enumerate(x_vec):
        lr *= (likelihoods[(1, i, val)] / likelihoods[(0, i, val)])
    label = 1 if (lr * (priors[1]/priors[0])) > 1 else 0
    return lr, label

# Test
test_vec = [1, 0, 1, 1, 1]
print(f"Posterior Distribution: {get_posterior(test_vec, priors, likelihoods)}")
print(f"Posterior Odds: {posterior_odds(test_vec)}")