import requests

URL = "https://api.zippopotam.us/us/"


def get_postcode(postcode):
    response = requests.get(f"{URL}{postcode}")

    if response.status_code == 200:
        print(response.content)
        return response
    else:
        return None


if __name__ == '__main__':
    get_postcode("33162")
