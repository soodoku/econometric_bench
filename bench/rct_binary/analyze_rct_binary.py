import pandas as pd
import statsmodels.api as sm

# Load the simulated data
rct_data = pd.read_csv("rct_simulated_data.csv")

# Analyze the experiment using a logistic regression model
X = sm.add_constant(rct_data['assignment'])  # Add intercept term
y = rct_data['binary_outcome']
model = sm.Logit(y, X)
result = model.fit()

# Extract effect size and standard error
effect = result.params['assignment']
std_error = result.bse['assignment']

# Display results
print("\nFinal Output:")
print(f"Effect size: {effect:.4f}")
print(f"Standard error: {std_error:.4f}")

