import matplotlib.pyplot as plt
import csv

# Initialize empty lists for the x and y data
x = []
y = []

# Open the CSV file and read the data
with open('100.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter='\t')  # Use tab as the delimiter
    for row in plots:
      if len(row) >= 2:
        x.append(float(row[0]))
        y.append(float(row[1]))

# Scatter plot with dotted markers



# Add a title and labels to the plot
plt.title('Locally Weighted Regression')
plt.xlabel('Total Bill')
plt.ylabel('Tip')

# Show the plot
plt.show()



import statsmodels.api as sm
lowess = sm.nonparametric.lowess(x,y, frac=.2)
lowess_x = list(zip(*lowess))[0]
lowess_y = list(zip(*lowess))[1]

plt.scatter(x,y, color='green')
plt.plot(lowess_y,lowess_x, color = 'red', linewidth=3)

