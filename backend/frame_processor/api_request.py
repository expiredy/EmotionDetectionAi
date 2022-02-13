import requests
from dotenv import dotenv_values

CONFIG = dotenv_values(".env")


def send_request_to_api(person_id: int, person_gender: str, person_age: int, person_mood: str):
    print("person id: ", person_id, "geydenr: ", person_gender, "my age: ", person_age, "person mooder: ", person_mood)
    try:
        response = requests.post(CONFIG["API_REQUEST_ADDRESS"], json={"Id": person_id,
                                                                      "Gender": person_gender,
                                                                      "Age": person_age,
                                                                      "Mood": person_mood})
        print(response.status_code)
    except requests.exceptions.ConnectionError:
        print("Anton is down")