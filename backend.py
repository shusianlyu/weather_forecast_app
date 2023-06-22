import requests
import config

API_KEY = config.API_KEY


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid" \
          f"={API_KEY}"
    response = requests.get(url)
    res = response.json()
    filtered_data = res['list']
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    return filtered_data


if __name__ == '__main__':
    print(get_data("Taipei", 2))
