def get_weather(city: str) -> str:
    samples = {
        "new york": "Sunny, 24°C",
        "london": "Cloudy, 18°C",
        "tokyo": "Rainy, 21°C",
        "sydney": "Windy, 20°C"
    }
    return samples.get(city.lower(), "Partly cloudy, 22°C")


def main():
    city = input("Enter a city name: ")
    forecast = get_weather(city)
    print(f"Weather for {city.title()}: {forecast}")


if __name__ == "__main__":
    main()
