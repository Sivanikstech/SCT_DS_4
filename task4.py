import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("archive/US_Accidents_March23.csv")

print(df.head())
print(df.info())

df = df[['Severity', 'Start_Time', 'Weather_Condition', 'Visibility(mi)', 'City']]

df['Start_Time'] = pd.to_datetime(df['Start_Time'], format='mixed', errors='coerce')

df['Hour'] = df['Start_Time'].dt.hour

df.dropna(inplace=True)

plt.figure()
sns.countplot(x='Hour', data=df)
plt.title("Accidents by Time of Day")
plt.xticks(rotation=90)
plt.savefig("accidents_by_hour.png", dpi=300, bbox_inches='tight')
plt.show()

plt.figure()
df['Weather_Condition'].value_counts().head(10).plot(kind='bar')
plt.title("Top Weather Conditions")
plt.savefig("weather_conditions.png", dpi=300, bbox_inches='tight')
plt.show()

plt.figure()
sns.countplot(x='Severity', data=df)
plt.title("Accident Severity")
plt.savefig("accident_severity.png", dpi=300, bbox_inches='tight')
plt.show()

plt.figure()
df['City'].value_counts().head(10).plot(kind='bar')
plt.title("Accident Hotspots (Cities)")
plt.savefig("accident_hotspots.png", dpi=300, bbox_inches='tight')
plt.show()