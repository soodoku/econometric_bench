### Data Generation Script with Clustered Assignment
import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# Parameters
n_clusters = 50  # Number of clusters
effect_size = 0.2  # Effect size in standard deviations

# Generate cluster sizes (vary dramatically)
cluster_sizes = np.random.randint(5, 50, size=n_clusters)
total_participants = sum(cluster_sizes)

# Assign treatment at the cluster level
cluster_assignment = np.random.choice([0, 1], size=n_clusters)

# Generate participant-level data
assignment = []
latent = []

for cluster, size in enumerate(cluster_sizes):
    treatment = cluster_assignment[cluster]
    assignment.extend([treatment] * size)
    if treatment == 0:
        # Control group
        latent.extend(np.random.normal(loc=0, scale=1, size=size))
    else:
        # Treatment group
        latent.extend(np.random.normal(loc=effect_size, scale=1, size=size))

# Convert to binary outcome using a threshold (e.g., median)
latent = np.array(latent)
assignment = np.array(assignment)
threshold = np.median(latent)
binary_outcome = (latent > threshold).astype(int)

# Create a DataFrame
rct_data = pd.DataFrame({
    'cluster': np.repeat(np.arange(n_clusters), cluster_sizes),
    'assignment': assignment,  # 0 for control, 1 for treatment
    'latent_outcome': latent,
    'binary_outcome': binary_outcome
})

# Save data to CSV
rct_data.to_csv("rct_clustered_simulated_data.csv", index=False)

