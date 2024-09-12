import numpy as np
from scipy.stats import entropy

# Logarithm base 2
def log2(x):
    return np.log2(x)

# Entropy Calculation: Given P(A) = 0.7, P(B) = 0.3
def entropy_calc(probabilities):
    return -np.sum([p * log2(p) for p in probabilities if p > 0])

# Conditional Entropy
def conditional_entropy(joint_probs, marginal_probs_b):
    cond_entropy = 0
    for b, p_b in enumerate(marginal_probs_b):
        if p_b > 0:
            p_a_given_b = joint_probs[:, b] / p_b
            cond_entropy += p_b * entropy_calc(p_a_given_b)
    return cond_entropy

# Joint Entropy
def joint_entropy(joint_probs):
    return -np.sum([p * log2(p) for p in joint_probs.flatten() if p > 0])

# Information Gain
def information_gain(H_total, H_splits, split_weights):
    return H_total - np.sum([w * h for w, h in zip(split_weights, H_splits)])

# Mutual Information
def mutual_information(H_a, H_b, H_ab):
    return H_a + H_b - H_ab

# Example for Question 1: Entropy Calculation
prob_dist = [0.7, 0.3]
H = entropy_calc(prob_dist)
print(f"Entropy of system: {H:.3f}")

# Example for Question 2: Conditional Entropy H(A|B)
joint_prob_matrix = np.array([[0.3, 0.1], [0.2, 0.4]])
marginal_prob_B = np.sum(joint_prob_matrix, axis=0)  # Marginal probability for B
H_A_given_B = conditional_entropy(joint_prob_matrix, marginal_prob_B)
print(f"Conditional Entropy H(A|B): {H_A_given_B:.3f}")

# Example for Question 3: Joint Entropy
H_AB = joint_entropy(joint_prob_matrix)
print(f"Joint Entropy H(A, B): {H_AB:.3f}")

# Example for Question 4: Information Gain
# Initial entropy H(Y)
H_Y = entropy_calc([0.6, 0.4])

# Split entropies H(Y|X)
H_Y_given_X1 = entropy_calc([0.75, 0.25])
H_Y_given_X2 = entropy_calc([0.5, 0.5])

# Weights of the splits
weights = [0.4, 0.6]  # Based on the size of the subsets

# Information gain
IG_X = information_gain(H_Y, [H_Y_given_X1, H_Y_given_X2], weights)
print(f"Information Gain after splitting on X: {IG_X:.3f}")

# Example for Question 5: Mutual Information
H_A = 1.0
H_A_given_B = 0.5
I_A_B = H_A - H_A_given_B
print(f"Mutual Information I(A;B): {I_A_B:.3f}")

# Example for Question 7: Mutual Information using Joint and Marginal Entropies
H_A = 1.0
H_B = 1.0
H_A_B = 1.5
I_A_B_joint = mutual_information(H_A, H_B, H_A_B)
print(f"Mutual Information based on joint entropy: {I_A_B_joint:.3f}")
