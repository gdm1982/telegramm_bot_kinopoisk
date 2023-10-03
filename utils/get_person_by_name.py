import requests
from loader import headers


def get_person_by_name(name, page=1, limit=1):
    """ Функция получает информацию о ближайшей похожей по названию медийной личности """
    response = requests.get(
        'https://api.kinopoisk.dev/v1.2/person/search',
        params={
            "query": name,
            "limit": limit,
            "page": page,
        },
        headers=headers
    )
    movies = response.json()
    return movies["docs"]


# Что планируется вывести (внесено в search_person_by_name.py):
# search = input('Имя: ')
# data = get_person_by_name(search)
# print(data[0]['name'])
# print(data[0]['enName'])
# print(data[0]['photo'])
# print(data[0]['sex'])
# print(data[0]['birthPlace'])
# print(data[0]['birthday'])
# print(data[0]['age'])
# print(data[0]['death'])
# print(data[0]['deathPlace'])
# print(data[0]['profession'])

# Вид ответа:
# [
#   {
#       'id': 10552,
#       'name': 'Майкл Бэй',
#       'enName': 'Michael Bay',
#       'photo': 'https://avatars.mds.yandex.net/get-kinopoisk-image/1946459/838aedee-dfa9-452c-9761-fa9a4b44db9f/orig',
#       'sex': 'Мужской',
#       'growth': 185,
#       'birthday': '1965-02-17T00:00:00.000Z',
#       'death': '',
#       'age': 58,
#       'birthPlace': ['Лос-Анджелес', 'Калифорния', 'США'],
#       'deathPlace': [],
#       'profession': ['Режиссер', 'Продюсер', 'Актер']
#   }
# ]
