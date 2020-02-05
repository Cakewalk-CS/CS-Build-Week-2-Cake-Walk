import random
import requests
import json
from key import API_KEY
import time

url = 'https://lambda-treasure-hunt.herokuapp.com/api'

headers = {
    'Authorization': API_KEY
}

def init():
    r = requests.get(f'{url}/adv/init/', headers=headers)
    print(r.json())


def move(payload):
    r_move = requests.post(f'{url}/adv/move', data=json.dumps(payload), headers=headers)
    save = r_move.json()
    print(save)

    data = {
        'room_id':  save['room_id'],
        'coordinates':  save['coordinates'],
        'exits':  save['exits'],
        'title': save['title'],
        'description': save['description'],
        'items': save['items'],
        'elevation': save['elevation'],
        'terrain': save['terrain']
    }
    
    current_state = get_contents()
    print('current_state', current_state)

    if str(save['room_id']) not in current_state.keys():
        current_state[save['room_id']] = data
        save_content(current_state)



def save_content(data):
    with open('map.txt', 'w') as f:
        f.write(json.dumps(data, indent=4))

def get_contents():
    map_file = open('map.txt', 'rb').read()
    contents = json.loads(map_file)
    return contents

# save_content({'a': 'aa111222'})
move({"direction":"e"})









