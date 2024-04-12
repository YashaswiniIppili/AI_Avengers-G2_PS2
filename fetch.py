import requests
import json

url = "https://data.g2.com/api/v1/survey-responses"
secret_token = "c5ec205a957353f5d655dca1529692f11dc1aab6e70b62563f6a475982ad99ad"


def fetch_data():
    headers = {
        "Authorization": f"Token token={secret_token}",
        "Content-Type": "application/vnd.api+json",
    }
    all_data = []
    page_number = 1
    while True:
        params = {"page[number]": page_number, "page[size]": 100}
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            data = response.json()
            if not data["data"]:
                break
            all_data.extend(data["data"])
            page_number += 1
        else:
            print(f"Failed to fetch data. Status code: {response.status_code}")
            return None
    return all_data


def main():
    data = fetch_data()
    if data:
        num_ids = len(data)
        print(f"Number of IDs: {num_ids}")

        with open("survey_responses.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Data has been successfully fetched and stored in survey_responses.json.")
    else:
        print("Failed to fetch and store data.")


if __name__ == "__main__":
    main()
