import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("C:\\Users\\kumar\\Downloads\\data_analysis\\covid_vaccine_statewise.csv")
# Remove India row
data = data[data["State"] != "India"]
x = data.head()
y = data.tail()
print(x)
print(y)
print(data)
print(data.describe())
# Calculate mean for all numeric columns
print(data.mean(numeric_only=True))
# Calculate standard deviation for all numeric columns
print(data.std(numeric_only=True))
df = data[['Updated On', 'State', 'Total Doses Administered']]
df.columns = ['Date', 'st', 'Dos']
print(df.head())
today = df[df.Date == '16/01/2021']
print(today.head())
# Sort by total doses
maxDose = today.sort_values(by='Dos', ascending=False)
print(maxDose)
# Top 5 States
tsd = maxDose[0:5]
print(tsd)
# Top 10 States
tsd = maxDose[0:10]
print(tsd)
plt.figure(figsize=(12,6))
sns.barplot(
    x='st',
    y='Dos',
    data=tsd,
    hue='st',

)
plt.title("Top 10 States by Total Vaccine Doses on 16/01/2021")
plt.xlabel("State")
plt.ylabel("Total Doses Administered")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()