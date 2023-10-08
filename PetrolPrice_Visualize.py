import pandas as pd
import matplotlib.pyplot as plt
from PetrolPrice_StateWise_API import PetrolPrice_StateWise_API as PPSW

class PetrolPrice_Visualize:

 def __init__(self):
   # Create an instance of the PetrolPrice_StateWise_API class
   self.api = PPSW()

 def api_call(self):
     # Call the API to retrieve data and save it to a CSV file
    return self.api.api_call()
 


# File path to the CSV containing petrol prices
csv_file_path = "PetrolPrice.csv"

# Read the CSV file 
df = pd.read_csv(csv_file_path)


# Find the maximum and minimum petrol prices
max_petrol_price_state = max(df['Petrol Price'])
min_petrol_price_state = min(df['Petrol Price'])
plt.figure(figsize=(12, 8))

# Iterate through the DataFrame to plot bars for each state
for i in range(len(df['State'])):

  if df['Petrol Price'][i] == max_petrol_price_state:
    plt.bar(df['State'][i], df['Petrol Price'][i], color = 'red')

  elif df['Petrol Price'][i] == min_petrol_price_state:
    plt.bar(df['State'][i],df['Petrol Price'][i],color='green')

  else:
    plt.bar(df['State'][i], df['Petrol Price'][i],color = 'orange')
    
  plt.text(df['State'][i], df['Petrol Price'][i] + 0.2, f'{df["Petrol Price"][i]:.2f}', ha='center')

# Set labels and title for the plot
plt.xlabel('City/State')
plt.ylabel('Price')
plt.title('Petrol and Diesel Prices by City/State')

# Rotate x-axis labels & adjusting layout for better visibility
plt.xticks(rotation=90)
plt.tight_layout()


# Show the plot
plt.show()



