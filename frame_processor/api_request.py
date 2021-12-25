import requests


def send_request_to_API(person_id: int, person_gender: str, person_age: int, person_mood: str):
    api_link = "http://62.109.14.86/api/neuronet/postinfo"
    response = requests.post(api_link, json={"Id": person_id,
                                             "Gender": person_gender,
                                             "Age": person_age,
                                             "Mood": person_mood})
    print(response.status_code)
