import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("C:\\Users\\kumar\\Downloads\\traffic_violation\\Indian_Traffic_Violations.csv")
print(data)
x=data.head()
y=data.tail()

print(data.describe())
print(data.mean(numeric_only=True))
print(data.std(numeric_only=True))

state_count = data['Location'].value_counts().reset_index()

# Rename columns
state_count.columns = ['Location', 'Violations']

print(state_count)

sns.barplot(x='Location',y='Violations',data=state_count, hue='Location')
plt.title('Traffic Violations ')
plt.show()