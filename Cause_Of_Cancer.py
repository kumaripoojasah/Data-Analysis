import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("C:\\Users\\kumar\\Downloads\\cancer_analysis\\Cancer_Statewise_Dataset.xlsx")

# Group by State
state_data = df.groupby("State")[["Diagnosed_Cases",
                                  "Cured_Cases",
                                  "Deaths",
                                  "Alive_Patients"]].sum()
print(state_data.describe())
print(state_data.mean(numeric_only=True))
print(state_data.std(numeric_only=True))
print(state_data)

# Plot
state_data.plot(kind="bar", figsize=(14,6))

plt.title("State-wise Cancer Analysis")
plt.xlabel("State")
plt.ylabel("Number of Patients")
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.show()