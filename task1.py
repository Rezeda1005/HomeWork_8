import requests

token = '2619421814940190'
superhero_list = ['Hulk', 'Thanos', 'Captain America']


def intelligence_compare(hero_list):
    super_man = []
    for hero in hero_list:
        url = f'https://www.superheroapi.com/api.php/{token}/search/{hero}'
        intelligence = requests.get(url).json()
        try:
            for power_stats in intelligence['results']:
                super_man.append({
                    'name': power_stats['name'],
                    'intelligence': power_stats['powerstats']['intelligence'],
                })
        except KeyError:
            print(f"Ошибка загрузки. Проверьте список супергероев: {hero_list}")

    intelligence_super_hero = 0
    name = ''
    for intelligence_hero in super_man:
        if intelligence_super_hero < int(intelligence_hero['intelligence']):
            intelligence_super_hero = int(intelligence_hero['intelligence'])
            name = intelligence_hero['name']

    print(f"Самый умный(intelligence) из трех супергероев: {name}, его интелект равен: {intelligence_super_hero}")


if __name__ == '__main__':

    intelligence_compare(superhero_list)

