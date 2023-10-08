import pandas as pd
import matplotlib.pyplot as plt
from PetrolPrice_StateWise_API import PetrolPrice_StateWise_API as PPSW

class PetrolPrice_Visualize:

 def __init__(self):
   self.api = PPSW()

 def api_call(self):
    return self.api.api_call()

csv_file_path = "PetrolPrice.csv"
df = pd.read_csv(csv_file_path)
max_petrol_price_state = max(df['Petrol Price'])
min_petrol_price_state = min(df['Petrol Price'])
plt.figure(figsize=(12, 8))

for i in range(len(df['State'])):
  if df['Petrol Price'][i] == max_petrol_price_state:
    plt.bar(df['State'][i], df['Petrol Price'][i], color = 'red')
  elif df['Petrol Price'][i] == min_petrol_price_state:
    plt.bar(df['State'][i],df['Petrol Price'][i],color='green')
  else:
    plt.bar(df['State'][i], df['Petrol Price'][i],color = 'orange')
    #plt.bar(df['State'], df['Diesel Price'], color='r', label='Diesel Price')
plt.xlabel('City/State')
plt.ylabel('Price')
plt.title('Petrol and Diesel Prices by City/State')
plt.xticks(rotation=90)
plt.tight_layout()

# Show the plot
plt.show()



