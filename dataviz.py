import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

bond_data = pd.read_csv("./referenced_data.csv")
football_data = pd.read_csv("./augmented_data.csv")

parties = bond_data.groupby("Party").agg({"Denominations": lambda x: x.sum()}).reset_index()
parties.sort_values(by="Denominations", ascending=False, inplace=True)

sns.set_style("darkgrid")
plt.style.use('https://github.com/dhaitz/matplotlib-stylesheets/raw/master/pitayasmoothie-dark.mplstyle')

# Basic Pie Chart with Matplotlib
plt.figure(figsize=(10, 5))
# plt.rcParams["font.size"] = 10
# plt.rcParams["font.stretch"] = "condensed"
plt.pie(parties["Denominations"], labels=parties["Party"])
plt.title('Share of Bond Encashments by Party', fontsize=14)
plt.show()

# Basic Scatter Plot with Matplotlib
plt.figure(figsize=(10, 5))
plt.scatter(football_data["location_x"], football_data["location_y"])
plt.scatter(football_data["goalkeeper_x"], football_data["goalkeeper_y"])
plt.title('Shooter and Goalkeeper Positions', fontsize=14)
plt.show()

# Basic Bar Chart with Pandas
ax = football_data["statsbomb_xg"].hist(bins=10, xlabelsize=10, ylabelsize=6, color="cyan")
ax.set_title('Distribution of shots by likelihood', weight='bold')
ax.set_xlabel('Likelihood')
ax.set_ylabel('Frequency')
plt.show()

# Basic Line Chart
copy = football_data.sort_values(by=["minute"])
plt.plot(copy["minute"], copy["possession"])
plt.title("Goalkeeper positions")
plt.show()
