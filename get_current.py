import requests
import csv
import pandas as pd

API_KEY = "T9N6LJR7EVGAWPK2DTMJUL9LT"


def get_weather_data(city):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/today?unitGroup=metric&elements=datetime%2CdatetimeEpoch%2Cname%2Ctempmax%2Ctempmin%2Ctemp%2Chumidity%2Cconditions&include=current&key={API_KEY}&contentType=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # JSON to pandas DataFrame
        current_data_list = data["currentConditions"]
        current_df = pd.Series(current_data_list)
        return current_df

    else:
        print(response.status_code)


cities = ["Kaunas", "Vilnius", "Klaipeda"]
for city in cities:
    data = get_weather_data(city)
    print(f"{city}: \n{data}")
