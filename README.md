# Weather Data Fetcher

This Python script fetches both current and historical weather data from the Visual Crossing Weather API for a list of specified cities. It returns the temperature (minimum, maximum, and average), humidity, and the general weather condition for the specified date range.


## Usage

This script fetches weather data for Kaunas, Vilnius, and Klaipeda by default and for the year 2023. If you want to change the cities or the date range, modify the `cities` list and the dates in the `get_weather_data` function call.

To get the current weather, use the following command:

```shell
python get_current.py
```

To get the historical weather, use the following command:

```shell
python get_historical.py
```

## Output

This script saves the weather data for each city to a CSV file named as `{city}_weather_data.csv` in the `data` directory. Each row in the CSV file represents one day and includes the following columns:

- datetime
- tempmax
- tempmin
- temp
- humidity
- conditions

## API Key

The script uses an API key for the Visual Crossing Weather API, which is stored in the `API_KEY` variable. If you want to use your own API key, replace the value of the `API_KEY` variable with your key.

## Error Handling

If the script encounters an error when making a request to the API, it will print the HTTP status code to the console.

## Dependencies

- Python
- requests
- pandas
