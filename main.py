import types

import requests
from pyfiglet import Figlet
import folium


def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        data = {
            '[IP]': response.get('query'),
            '[provider]': response.get('isp'),
            '[organisation]': response.get('org'),
            '[region name]': response.get('regionName'),
            '[city]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[lat]': response.get('lat'),
            '[lon]': response.get('lon'),
        }
        if type(response.get('lat')) == types.NoneType:
            print('bad ip')
        else:
            for k, v in data.items():
                print(f'{k} : {v}')
            area = folium.Map(location=[response.get('lat'), response.get('lon')])
            area.save(f'{response.get("query")}_{response.get("city")}.html')
    except requests.exceptions.ConnectionError:
        print('[!]Check your connection!')
    get_info_by_ip(ip=input_text())


def input_text():
    return input('Please enter a target IP: ')


def main():
    preview_text = Figlet(font='slant')
    print(preview_text.renderText('ip info'))

    get_info_by_ip(ip=input_text())


if __name__ == '__main__':
    main()
