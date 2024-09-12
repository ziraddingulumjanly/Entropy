### Entropy Formula

In information theory, entropy is a measure of the uncertainty or unpredictability of a random variable. It quantifies the amount of information required to describe the outcome of a probabilistic process. Higher entropy means higher unpredictability.

The formula for the entropy $H(X)$ of a discrete random variable $X$, which takes values $x_1, x_2, \dots, x_n$ with probabilities $P(x_1), P(x_2), \dots, P(x_n)$, is given by:

$$
H(X) = - \sum_{i=1}^{n} P(x_i) \log_b P(x_i)
$$

Where:
- $H(X)$ is the entropy of the random variable $X$.
- $P(x_i)$ is the probability of each possible outcome $x_i$.
- $\log_b$ represents the logarithm to the base $b$, which is commonly base 2 (for entropy measured in bits), base $e$ (natural logarithm, for nats), or base 10.
- The summation $\sum$ runs over all possible outcomes $x_i$ of the random variable $X$.

Entropy provides a fundamental limit on the best possible lossless compression of any communication, in bits per symbol for base-2 logarithms.
