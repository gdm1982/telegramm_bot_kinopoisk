import requests
from loader import headers


def get_movie_by_name(name, page=1, limit=1):
    """ Функция получает информацию о ближайшем похожем по названию фильме или сериале """
    response = requests.get(
        'https://api.kinopoisk.dev/v1.2/movie/search',
        params={
            "query": name,
            "limit": limit,
            "page": page,
        },
        headers=headers
    )
    movies = response.json()
    return movies["docs"]


# Что планируется вывести (внесено в search_movie_by_name.py):
# search = input('Название фильма/сериала: ')
# data = get_movie_by_name(search)
# print(data[0]['name'])
# print(data[0]['alternativeName'])
# print(data[0]['type'])
# print(data[0]['year'])
# print(data[0]['shortDescription'])
# print(data[0]['poster'])
# print(data[0]['rating'])
# print(data[0]['genres'])
# print(data[0]['countries'])

# Вид ответа:
# [
# 	{
# 	    'id': 251733,
# 	    'name': 'Аватар',
# 	    'alternativeName': 'Avatar',
# 	    'enName': '',
# 	    'names': ['Аватар', 'Avatar', 'Project 880465wtgsdtg', 'Avatar Edicion Coleccionista',
# 	    'Avatar: Extended Version', "Avatar - Collector's Extended Edition",
# 	    'Avatar - Edição Estendida de Colecionador', 'Avatar 3D', 'Avatar: An IMAX 3D Experience', ...],
# 	    'type': 'movie',
# 	    'year': 2009,
# 	    'description': 'Бывший морпех Джейк Салли прикован к\xa0инвалидному креслу. Несмотря на\xa0немощное тело, ...',
# 	    'shortDescription': 'Парализованный морпех становится мессией для жителей Пандоры.
# 	                         Самый кассовый фильм в истории кино\n',
# 	    'logo': 'https://avatars.mds.yandex.net/get-ott/2385704/2a00000176f1bb64212c9df414a8909c8f44/orig',
# 	    'poster': 'https://st.kp.yandex.net/images/film_big/251733.jpg',
# 	    'backdrop': 'https://avatars.mds.yandex.net/get-ott/374297/2a000001616b87458162c9216ccd5144e94d/orig',
# 	    'rating': 7.971,
# 	    'votes': 983386,
# 	    'movieLength': 162,
# 	    'genres': ['фантастика', 'боевик', 'драма', 'приключения'],
# 	    'countries': ['США'],
# 	    'releaseYears': []
# 	 }
# ]
