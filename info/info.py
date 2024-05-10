import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv('equal.csv')

# Drop the 'Record' column
data.drop(columns=['Record'], inplace=True)

# Find the best record
best_record = data[data['Score'] == data['Score'].max()]

# Plot Game against Score
plt.figure(figsize=(10, 6))
plt.plot(data['Game'], data['Score'], marker='o', linestyle='-')
plt.scatter(best_record['Game'], best_record['Score'], color='red', label='Best Record')
plt.xlabel('Game')
plt.ylabel('Score')
plt.title('Game Scores')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()

# Export the plot as a PNG file
plt.savefig('equal.png')

# Show the plot
plt.show()
