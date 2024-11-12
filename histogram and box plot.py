import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
data = pd.read_csv("D:/advanced Analystics/DBDA-AtulKahate/tips.csv")
print(data.head())

# Descriptive statistics
tip_stats = data['tip'].describe()
print("Descriptive Statistics for the 'tip' column:")
print(tip_stats)

# Additional statistics
mean_tip = data['tip'].mean()
median_tip = data['tip'].median()
std_tip = data['tip'].std()
var_tip = data['tip'].var()
skew_tip = data['tip'].skew()
cv_tip = (std_tip / mean_tip) * 100

print("\nAdditional Statistics for the 'tip' column:")
print(f"Mean: {mean_tip}")
print(f"Median: {median_tip}")
print(f"Standard Deviation: {std_tip}")
print(f"Variance: {var_tip}")
print(f"Skewness: {skew_tip}")
print(f"Coefficient of Variation: {cv_tip}%")

# Plotting
plt.figure(figsize=(14,6))

# Histogram
plt.subplot(1, 2, 1)
sns.histplot(data['tip'], bins=20, kde=True)
plt.title('Distribution of Tips')
plt.xlabel('Tip Amount')
plt.ylabel('Frequency')

# Box plot
plt.subplot(1, 2, 2)
sns.boxplot(x=data['tip'])
plt.title('Box Plot of Tips')
plt.xlabel('Tip Amount')

plt.tight_layout()
plt.show()
