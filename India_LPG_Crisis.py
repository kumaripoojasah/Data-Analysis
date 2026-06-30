import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("C:\\Users\\kumar\\Downloads\\lpg_analysis\\LPG_Statewise_Migration_Dataset.csv")   # Change to your file path

# Group by State
state_data = df.groupby("State")[[
    "LPG_Consumption_MMT",
    "LPG_Shortage_MMT",
    "People_Migrated"
]].sum()

print(state_data)


# Crisis Level

high = state_data["LPG_Shortage_MMT"].quantile(0.75)
medium = state_data["LPG_Shortage_MMT"].quantile(0.50)

def crisis_level(shortage):
    if shortage >= high:
        return "High"
    elif shortage >= medium:
        return "Medium"
    else:
        return "Low"

state_data["Crisis_Level"] = state_data["LPG_Shortage_MMT"].apply(crisis_level)

print(state_data)


# Highest Crisis State
highest = state_data["LPG_Shortage_MMT"].idxmax()
print("\nHighest Crisis State :", highest)

# Lowest Crisis State
lowest = state_data["LPG_Shortage_MMT"].idxmin()

print("Lowest Crisis State :", lowest)



plt.figure(figsize=(15,6))

plt.bar(state_data.index,
        state_data["LPG_Shortage_MMT"])

plt.title("State-wise LPG Shortage")
plt.xlabel("State")
plt.ylabel("LPG Shortage (MMT)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

