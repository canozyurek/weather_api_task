import requests
import csv
import pandas as pd

API_KEY = "NPCVWL8B9WT88R43RXV8WF7BZ"


def get_weather_data(city, start_date, end_date):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/{start_date}/{end_date}?unitGroup=metric&elements=datetime%2CdatetimeEpoch%2Cname%2Ctempmax%2Ctempmin%2Ctemp%2Chumidity%2Cconditions&key={API_KEY}&contentType=json"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        # JSON to pandas DataFrame
        historical_data_list = data["days"]
        historical_df = pd.DataFrame(historical_data_list)
        historical_df = historical_df[
            ["datetime", "tempmax", "tempmin", "temp", "humidity", "conditions"]
        ]
        return historical_df

    else:
        print(response.status_code)


def save_to_csv(city, data):
    data.to_csv(f"data/{city}_weather_data.csv")


cities = ["Kaunas", "Vilnius", "Klaipeda"]
for city in cities:
    data = get_weather_data(city, "2023-01-01", "2023-12-31")
    save_to_csv(city, data)
