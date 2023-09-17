import requests
import dotenv
import os
import pprint

dotenv.load_dotenv()


def getCurrentWeather():
    print("\n*********Getting current weather**********\n")
    city = input("\nEnter city name: \n")

    requests_url = f"https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=imperial"

    response = requests.get(requests_url).json()
    # pprint.pprint(response)
    print(f"\nCurrent Weather for {response['name']}")
    print(f"\nThe temp is {response['main']['temp']}")
    print(f"The weather is {response['weather'][0]['description']}")


getCurrentWeather()
