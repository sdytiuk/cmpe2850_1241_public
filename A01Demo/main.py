import requests
import json


if __name__ == '__main__':
    form_params = {'Name': 'Wilson', 'Grades[]': [1,2,3]}
    response = requests.post('https://thor.cnt.sast.ca/~demo/cmpe2000/ica10_jsonResponse.php',data=form_params)
    print(response)
    if response.status_code == requests.codes.ok :
        print(response.text)
        stuff = response.json()
        print(f"How many rows of data? {len(stuff['data'])}")

