import requests

# Задание №1


def max_intelligence_power(name1, name2, name3):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    html_content = response.json()
    intelligence_power = {name1: 0, name2: 0, name3: 0}
    for _ in html_content:
        if _['name'] == name1:
            intelligence_power[name1] = _['powerstats']['intelligence']
        elif _['name'] == name2:
            intelligence_power[name2] = _['powerstats']['intelligence']
        elif _['name'] == name3:
            intelligence_power[name3] = _['powerstats']['intelligence']
    return max(intelligence_power.keys())

print(f'The cleverest superhero is {max_intelligence_power("Hulk", "Captain America", "Thanos")}!')

# Задание №2

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {
            'Authorization': f'OAuth {self.token}'
        }
        params = {
            'path': 'myfiles/test.txt'
        }
        with open(file_path, 'rb') as f:
            response = requests.get(url, headers=headers, params=params)
            upload = response.json()
            href = upload['href']
            response = requests.put(href, data=f)
            if response.status_code == 201:
                print('Файл успешно загружен на Яндекс диск')
            else:
                print('Произошла ошибка при загрузке файла')


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = ...
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)