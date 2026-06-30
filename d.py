import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\kumar\\Downloads\\traffic_violation\\Indian_Traffic_Violations.csv")

# Count violations for each location
state_count = data['Location'].value_counts().reset_index()

# Rename columns
state_count.columns = ['Location', 'Violations']

print(state_count)

plt.figure(figsize=(12,6))

sns.barplot(
    data=state_count,
    x='Location',
    y='Violations'
)

plt.xticks(rotation=90)
plt.xlabel("Location")
plt.ylabel("Number of Violations")
plt.title("Traffic Violations by Location")

plt.show()