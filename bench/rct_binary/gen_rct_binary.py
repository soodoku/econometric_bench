import numpy as np
import pandas as pd
from scipy.stats import norm

# Set seed for reproducibility
np.random.seed(42)

# Parameters
n_per_group = 500  # Number of participants per group
effect_size = 0.2  # Effect size in standard deviations

# Generate treatment assignment
n_total = n_per_group * 2
assignment = np.array([0] * n_per_group + [1] * n_per_group)

# Generate potential outcomes (latent variable)
# Standard normal for control group, shifted normal for treatment group
control_mean = 0
treatment_mean = effect_size

latent_control = np.random.normal(loc=control_mean, scale=1, size=n_per_group)
latent_treatment = np.random.normal(loc=treatment_mean, scale=1, size=n_per_group)

latent = np.concatenate([latent_control, latent_treatment])

# Convert latent variable to binary outcome using a threshold (e.g., median)
threshold = np.median(latent)
binary_outcome = (latent > threshold).astype(int)

# Create a DataFrame
rct_data = pd.DataFrame({
    'assignment': assignment,  # 0 for control, 1 for treatment
    'latent_outcome': latent,
    'binary_outcome': binary_outcome
})

# Display summary
summary = rct_data.groupby('assignment')['binary_outcome'].mean()

print("\nSummary of binary outcomes by group:")
print(summary)

# Save data to CSV (optional)
# rct_data.to_csv("rct_simulated_data.csv", index=False)
