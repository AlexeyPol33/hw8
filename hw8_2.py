
import requests
import os

def upload(url,token,file_way,file_name):
    params = dict(path = file_name, overwrite='replace')
    headers = {'Authorization': f'OAuth {token}'}
    get_url = requests.get(url=url,headers=headers,params=params).json()['href']
    with open(file_way) as f:
        requests.put(get_url,files={'file':f})
    return 
if __name__ == '__main__':
    yandex_token = '' # Токен яндекс диска
    file_name = 'test_file.txt'
    file_way = os.path.abspath(file_name)
    url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'

    print(upload(url,yandex_token,file_way,file_name))
