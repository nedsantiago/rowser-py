import requests
from requests import Response


def get_request(url: str) -> str:
    """
    Makes a request to the provided url parameter. Returns a string of HTML
    data.
    """

    try:
        response: Response = requests.get(url)
    except ValueError as e:
        raise e

    print(f"{response.encoding=}")
    print(f"{type(response.content)=}")
    # Return string data
    return response.text

# Add HTTP checks here, e.g. what to do for each failure mode
