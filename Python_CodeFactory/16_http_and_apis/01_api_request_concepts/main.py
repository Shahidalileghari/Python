from urllib.error import URLError
from urllib.request import Request, urlopen
import json


def main() -> None:
    # Public demo endpoint; requires an internet connection.
    url = "https://jsonplaceholder.typicode.com/todos/1"
    request = Request(url, headers={"User-Agent": "Python-CodeFactory-Lesson"})

    try:
        with urlopen(request, timeout=8) as response:
            if response.status != 200:
                print("Unexpected HTTP status:", response.status)
                return
            payload = json.loads(response.read().decode("utf-8"))
        print("Title:", payload.get("title"))
        print("Completed:", payload.get("completed"))
    except (URLError, TimeoutError, json.JSONDecodeError) as error:
        print("Request failed:", error)


if __name__ == "__main__":
    main()
