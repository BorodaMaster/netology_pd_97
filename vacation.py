import requests
import time


def find_uk_city(coordinates:list) -> str:
    url = "https://geocode.maps.co/reverse?"
    uk_cites = ("Leeds", "London", "Liverpool", "Manchester", "Oxford", "Edinburgh", "Norwich", "York")

    for lat, lon in coordinates:
        resp = requests.get(f"{url}lat={lat}&lon={lon}")
        city_info = resp.json()
        city = city_info["address"]["city"]

        if city in uk_cites:
            return city
        else:
            time.sleep(10)
            continue


if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'
