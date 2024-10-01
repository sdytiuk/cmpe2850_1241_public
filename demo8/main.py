import os
import numpy as np
import requests
import json

from itertools import permutations, count, cycle, repeat
from matplotlib import pyplot as plt

if __name__ == '__main__':
    params = 'name=Willy&word=Wonky'
    form_params = {'tagId':'all'}
    response = requests.post('https://thor.cnt.sast.ca/~demo/cmpe2000/lab03_webservice.php',data=form_params)
    if response.status_code == requests.codes.ok:
        print(response.text)
        stuff = response.json()
        data = stuff['data']
        print(f'Number of rows returned: {len(data)}')
        for row in data:
            print(f"{row['tagId']}:{row['tagDescription']}")

    print(response.status_code)

