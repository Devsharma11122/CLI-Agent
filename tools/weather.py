import requests


def get_weather(city: str):

    url = f"https://wttr.in/{city}?format=j1"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    current = data["current_condition"][0]

    return {
        "city": city,
        "temperature": current["temp_C"],
        "condition": current["weatherDesc"][0]["value"]
    }