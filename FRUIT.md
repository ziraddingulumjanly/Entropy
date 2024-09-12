### Example: Low Entropy

Let's say you have a dataset with the following distribution of classes:

- **90% apples**
- **10% oranges**

The data is very predictable since most of it belongs to one category (apples). This represents **low entropy**.

- **Probability of apple, P(apple) = 0.9**
- **Probability of orange, P(orange) = 0.1**

Now, let's calculate the entropy using the formula:

$$
H(X) = - \sum P(x_i) \log_2 P(x_i)
$$

For this dataset:

$$
H(X) = - \left( 0.9 \log_2 0.9 + 0.1 \log_2 0.1 \right)
$$

Breaking it down:

- \( 0.9 \log_2 0.9 \approx -0.136 \)
- \( 0.1 \log_2 0.1 \approx -0.332 \)

So, the total entropy is:

$$
H(X) \approx 0.468
$$

This low entropy indicates that the data is **fairly predictable**.

---

### Example: High Entropy

Now, let’s look at a case where the data is more balanced and diverse:

- **50% apples**
- **50% oranges**

The data is less predictable since it is evenly split between two categories. This represents **high entropy**.

- **Probability of apple, P(apple) = 0.5**
- **Probability of orange, P(orange) = 0.5**

Again, applying the entropy formula:

$$
H(X) = - \left( 0.5 \log_2 0.5 + 0.5 \log_2 0.5 \right)
$$

Breaking it down:

- \( 0.5 \log_2 0.5 = -0.5 \)

So, the total entropy is:

$$
H(X) = 1.0
$$

This high entropy means that the data is **completely uncertain and random**, as it's equally split between apples and oranges.

---

### Conclusion with Numbers

- **Low entropy**: \( H(X) \approx 0.468 \) (90% apples, 10% oranges — more predictable).
- **High entropy**: \( H(X) = 1.0 \) (50% apples, 50% oranges — more uncertain).

This demonstrates how low entropy is associated with more predictability and high entropy with more randomness in a dataset.
