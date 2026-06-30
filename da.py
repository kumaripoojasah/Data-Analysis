import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("C:\\Users\\kumar\\Downloads\\data_analysis\\covid_vaccine_statewise.csv")
x=data.head()
y=data.tail()
print(data)
print(data.describe())
# Calculate mean for all numeric columns
print(data.mean(numeric_only=True))

# Calculate standard deviation for all numeric columns
print(data.std(numeric_only=True))
df=data[['Updated On','State','Total Doses Administered']]
df.columns=['Date','st','Dos']
print(df.head())
today =df[df.Date=='16/01/2021']
print(today.head())
maxDose=today.sort_values(by='Dos',ascending=False)
print(maxDose)

tsd=maxDose[0:5]
print(tsd)
tsd=maxDose[0:10]
print(tsd)

sns.barplot(x='st',y='Dos',data=tsd, hue='st')
plt.show()
