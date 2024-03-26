import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bond_data = pd.read_csv("./referenced_data.csv")
football_data = pd.read_csv("./augmented_data.csv")

print(bond_data.head())
print(football_data.head())

sns.set_style("darkgrid")
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')

# Basic Bar Chart
ax = football_data["statsbomb_xg"].hist(bins=10, xlabelsize=10, ylabelsize=6, color="cyan")
ax.set_title('Distribution of shots by likelihood', weight='bold')
ax.set_xlabel('Likelihood')
ax.set_ylabel('Frequency')
plt.show()
