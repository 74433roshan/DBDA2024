import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Data as a DataFrame
computer_time = pd.DataFrame({'Minutes': [16,8,35,17,13,15,15,5,16,25,20,20,12,10,55,30,40,45,8,78,54,]})

plt.figure(figsize=(10,6))
sns.boxplot(data=computer_time, orient='h', x='Minutes')

plt.title("BoxPlot of Computer Times")
plt.xlabel("Minutes")
plt.show()
