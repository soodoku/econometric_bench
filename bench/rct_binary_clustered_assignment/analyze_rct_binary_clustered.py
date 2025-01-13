import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.weightstats import DescrStatsW
from statsmodels.genmod.generalized_linear_model import GLM
from statsmodels.genmod.families import Binomial

# Load the simulated data
rct_data = pd.read_csv("rct_clustered_simulated_data.csv")

# Group by cluster to calculate means within clusters
cluster_means = rct_data.groupby('cluster').mean().reset_index()

# Define independent and dependent variables
X = sm.add_constant(cluster_means['assignment'])  # Add intercept term
y = cluster_means['binary_outcome']

# Fit a Generalized Linear Model (GLM) with Binomial family
model = GLM(y, X, family=Binomial())
result = model.fit()

# Extract effect size and standard error
effect = result.params['assignment']
std_error = result.bse['assignment']

# Display results
print("\nClustered Analysis Results:")
print(f"Effect size: {effect:.4f}")
print(f"Standard error: {std_error:.4f}")


