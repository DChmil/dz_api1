import requests

def test_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    json_datas = response.json()
    super_name = ['Hulk', 'Captain America', 'Thanos']
    intelligence = 0

    for data in json_datas:
        for super in super_name:
            if super == data['name'] and intelligence < data['powerstats']['intelligence']:
                final_name = data['name']
                intelligence = data['powerstats']['intelligence']
    return final_name


if __name__ == '__main__':
    print(test_request())