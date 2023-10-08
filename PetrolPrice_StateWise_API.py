
import requests
import pandas as pd
import matplotlib.pyplot as plt

class PetrolPrice_StateWise_API:

  def api_call(self):

    url = "https://all-daily-fuel-prices-india.p.rapidapi.com/ET_Calculators/oilpricebycitystate.htm"

    querystring = {"type":"state"}

    headers = {
	  "X-RapidAPI-Key": "58fb6e1e42msh05fe84d03cc7df7p1f8bf4jsn7463a85ab12c",
	  "X-RapidAPI-Host": "all-daily-fuel-prices-india.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data_json = response.json()

    data = []
    for result in data_json['results']:
     data.append({
        'State': result['cityState'],
        'Petrol Price': result['petrolPrice'],
        'Diesel Price': result['dieselPrice']
     })

    df = pd.DataFrame(data)

    datapath = "PetrolPrice.csv"
    df.to_csv(datapath, index=False)

# Display the DataFrame
  

