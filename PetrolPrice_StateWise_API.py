
import requests
import pandas as pd
import matplotlib.pyplot as plt

class PetrolPrice_StateWise_API:

  def api_call(self):

    #API endpoint URL
    url = "https://all-daily-fuel-prices-india.p.rapidapi.com/ET_Calculators/oilpricebycitystate.htm"

    # Query parameters for the API call
    querystring = {"type":"state"}

    # Headers for the API request
    headers = {
	  "X-RapidAPI-Key": "58fb6e1e42msh05fe84d03cc7df7p1f8bf4jsn7463a85ab12c",
	  "X-RapidAPI-Host": "all-daily-fuel-prices-india.p.rapidapi.com"
    }

    # Send API request and get response
    response = requests.get(url, headers=headers, params=querystring)

    
    # Parse response data as JSON
    data_in_json = response.json()

    # Prepare data from the JSON response
    data = []
    for result in data_in_json['results']:
     data.append({
        'State': result['cityState'],
        'Petrol Price': result['petrolPrice'],
        'Diesel Price': result['dieselPrice']
     })

    # Create a DataFrame from the extracted data
    dataframe = pd.DataFrame(data)

    # Specify the file path to save the DataFrame as a CSV
    datapath = "PetrolPrice.csv"

    # Save the DataFrame to a CSV file
    dataframe.to_csv(datapath, index=True)

  

